use pyo3::prelude::*;
use std::f32::consts::PI;
use std::ops::Index;
use std::sync::{Arc, Mutex};
use std::thread;
use std::thread::Thread;

fn normalize_angle(angle: f32) -> f32 {
    let mut result = angle;
    while result < 0.0 {
        result += 2.0 * PI;
    }
    while result >= 2.0 * PI {
        result -= 2.0 * PI;
    }
    result
}

fn distance(pnt1: (f32, f32), pnt2: (f32, f32)) -> f32 {
    f32::sqrt((pnt1.0 - pnt2.0).powi(2) + (pnt1.1 - pnt2.1).powi(2))
}

///     num_threads: usize,
///     playerX: f32,
///     playerY: f32,
///     player_angle: f32,
///     fov: f32,
///     screen_width: usize,
///     TILE_SIZE: f32,
///     SCALE: usize,
///     RENDER_DIST:usize,
///     render: Vec<u16>,
///     map: Vec<Vec<u16>>
#[pyfunction]
fn cast(
    py: Python,
    num_threads: usize,
    playerX: f32,
    playerY: f32,
    player_angle: f32,
    fov: f32,
    screen_width: usize,
    TILE_SIZE: f32,
    SCALE: usize,
    RENDER_DIST:usize,
    render: Vec<u16>,
    map: Vec<Vec<u16>>
) -> PyResult<Vec<(usize, (f32, f32), f32)>> {
    let rays: Arc<Mutex<Vec<(usize, (f32, f32), f32)>>> = Arc::new(Mutex::new(
        Vec::with_capacity(screen_width/SCALE)
    ));
    let render = Arc::new(render);
    let map = Arc::new(map);

    let angle_start = normalize_angle(player_angle - fov / 2.0);
    let angle_per_cont = normalize_angle(fov / (screen_width/SCALE) as f32);

    py.allow_threads(|| {
        let mut handles = vec![];
        for i in 0..num_threads {
            let rays = rays.clone();
            let render = render.clone();
            let map = map.clone();


            let handle  = thread::spawn(move || {
                let sum = angle_per_cont * (((screen_width/SCALE)/num_threads) as f32) * i as f32;
                let mut angle_ray = normalize_angle(angle_start + sum);

                for cont in (((screen_width/SCALE)/num_threads)*i)..(((screen_width/SCALE)/num_threads)*(i+1)) {
                // Calc horizontal -=-=-=-=-=-=-=--=-=-=-=-
                let ray_posi_h: (f32, f32);
                {
                    let aTan:f32 = -1.0 / (f32::tan(angle_ray) + 0.000001);
                    let mut ray_x:    f32;
                    let mut ray_y:    f32;
                    let mut offset_x: f32 = 0.0;
                    let mut offset_y: f32 = 0.0;
                    let mut rendist:  usize = 0;

                    if angle_ray > PI { // loking up
                        ray_y = (((playerY / TILE_SIZE) as i32) as f32) * TILE_SIZE - 0.0001;
                        ray_x = playerX + ((playerY - ray_y) * aTan);
                        offset_y = -TILE_SIZE;
                        offset_x = -offset_y * aTan;
                    } else if angle_ray < PI { // loking down
                        ray_y = (((playerY / TILE_SIZE) as i32) as f32) * TILE_SIZE + TILE_SIZE;
                        ray_x = playerX + ((playerY - ray_y) * aTan);
                        offset_y = TILE_SIZE;
                        offset_x = -offset_y * aTan;
                    } else {
                        ray_y = playerY;
                        ray_x = playerX;
                        rendist = RENDER_DIST
                    }

                    while rendist < RENDER_DIST {
                        let y = (ray_y/TILE_SIZE) as usize;
                        if !(y < 0 || y >= map.len()) {
                            let x = (ray_x/TILE_SIZE) as usize;
                            if !(x < 0 || x >= map[y].len()) {
                                if render.contains(&map[y][x]) {
                                    break
                                }
                            }
                        }
                        ray_x += offset_x;
                        ray_y += offset_y;
                        rendist += 1;
                    }
                    ray_posi_h = (ray_x, ray_y)
                }
                // Calc horizontal -=-=-=-=-=-=-=--=-=-=-=-
                // Calc vertical -=-=-=-=-=-=-=--=-=-=-=-
                let ray_posi_v: (f32, f32);
                {
                    let aTan:f32 = -f32::tan(angle_ray);
                    let mut ray_x: f32;
                    let mut ray_y: f32;
                    let mut offset_x: f32 = 0.0;
                    let mut offset_y: f32 = 0.0;
                    let mut rendist: usize = 0;

                    if angle_ray < PI/2.0 || angle_ray > 3.0*PI/2.0 { // loking rigth
                        ray_x = (((playerX / TILE_SIZE) as i32) as f32) * TILE_SIZE + TILE_SIZE;
                        ray_y = playerY + ((playerX - ray_x) * aTan);
                        offset_x = TILE_SIZE;
                        offset_y = -offset_x * aTan;
                    } else if angle_ray > PI/2.0 && angle_ray < 3.0*PI/2.0 { //loking left
                        ray_x = (((playerX / TILE_SIZE) as i32) as f32) * TILE_SIZE - 0.0001;
                        ray_y = playerY + ((playerX - ray_x) * aTan);
                        offset_x = -TILE_SIZE;
                        offset_y = -offset_x * aTan;
                    } else {
                        ray_y = playerY;
                        ray_x = playerX;
                        rendist = RENDER_DIST
                    }

                    while rendist < RENDER_DIST {
                        let y = (ray_y/TILE_SIZE) as usize;
                        if !(y < 0 || y >= map.len()) {
                            let x = (ray_x/TILE_SIZE) as usize;
                            if !(x < 0 || x >= map[y].len()) {
                                if render.contains(&map[y][x]) {
                                    break
                                }
                            }
                        }
                        ray_x += offset_x;
                        ray_y += offset_y;
                        rendist += 1;
                    }
                    ray_posi_v = (ray_x, ray_y);
                }
                // Calc vertical -=-=-=-=-=-=-=--=-=-=-=-

                let dist_h = distance(ray_posi_h, (playerX, playerY));
                let dist_v = distance(ray_posi_v, (playerX, playerY));

                let point: (f32, f32);
                let size:f32;
                if dist_h < dist_v {
                    point = ray_posi_h;
                    size = dist_h;
                }else {
                    point = ray_posi_v;
                    size = dist_v;
                }

                rays.lock().unwrap().push((cont, point, f32::cos(player_angle - angle_ray) * size));
                angle_ray += angle_per_cont;
                angle_ray = normalize_angle(angle_ray);
            }

            });
            handles.push(handle);
        }

        for handle in handles {
            handle.join().unwrap();
        }
    });



    let t = rays.lock().unwrap().to_vec();
    Ok(t)
}

/// A Python module implemented in Rust.
#[pymodule]
fn fast_ray_cast(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(cast, m)?)?;
    Ok(())
}