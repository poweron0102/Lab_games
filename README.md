# Cellular Odyssey: The Microcosm Quest

**High Concept**

*Cellular Odyssey: The Microcosm Quest* is a game where the player takes on the role of an immune system cell in the human body. They will have to perform their functions to protect the body from unknown substances such as germs, bacteria, parasites, and even cedar pollen, if necessary. In addition to germs, the player will also have to deal with everyday situations in our cells, like closed veins for maintenance and avoiding overzealous combat against intruders, which could lead to autoimmune reactions and allergies.

## Gameplay Flow

The player's main function is to keep the body healthy while eliminating pathogens. All levels take place within a body that is under attack by external substances.

- You will have to search for and eliminate invaders using neutrophils.
- Capture antigens and deliver them to dendritic cells with macrophages.
- Finally, exterminate the invaders throughout the body using the adaptive immune system with B lymphocytes and T lymphocytes.

Of course, when the adaptive immune system comes into play, the player must be careful not to kill healthy cells of the body and avoid excessive killing to prevent autoimmune reactions or allergies.

## Game Objects and Behaviors

1. **Player (Immune Cell):**
   - The player controls different types of immune cells, such as neutrophils, macrophages, B lymphocytes, and T lymphocytes, depending on the game's stage.
   - They can move through the body's environment to combat invaders and fulfill specific stage objectives.

2. **Antigens:**
   - These are unknown substances like germs, bacteria, parasites, and cedar pollen that invade the body.
   - The player must locate and eliminate antigens using neutrophils at the beginning of each stage.
   - Later, the player collects antigens to present them to dendritic cells.

3. **Dendritic Cells:**
   - NPCs that receive antigens from macrophages.
   - Their role is to present bacteria and fragments of infected cells as antigens to notify other immune cells.

4. **Neutrophils:**
   - They are the player's first line of defense.
   - Abilities include "Radar" (passive speed boost when approaching antigens representing histamine action) and "Neutrophilic Transmigration" (ability to cross some walls for a limited time).
   - They must locate and eliminate invaders at the beginning of each stage.

5. **Macrophages:**
   - Slower than neutrophils but highly lethal.
   - Possess the "Identification" ability, counting antigens and presenting them to dendritic cells.
   - Eliminate invaders and collect antigens for later presentation.

6. **Adaptive Immune System:**
   - Activates after the player collects and presents antigens to dendritic cells.
   - Comprises B lymphocytes and T lymphocytes, which are controlled by the player.

7. **B Lymphocytes:**
   - Move at the same speed as neutrophils.
   - Attack from a distance with their antibody weapons.
   - Have the "Guide" ability to direct T lymphocytes to the target.
   - Used to eliminate invaders after the adaptive immune system is activated.

8. **T Lymphocytes:**
   - Professional assassins capable of identifying and destroying foreign substances, such as virus-infected cells and cancerous cells.
   - Implanted under the guidance of helper T lymphocytes.
   - Act as NPCs to assist the player while playing as B lymphocytes.

9. **Closed Veins:**
   - Environmental objects that can be temporarily closed for maintenance.
   - The player must avoid causing excessive damage to these veins to prevent autoimmune reactions or allergies.

10. **Autoimmune Reactions and Allergies:**
    - Gameplay mechanics that penalize the player if they cause excessive damage to healthy cells or trigger adverse reactions in the body.