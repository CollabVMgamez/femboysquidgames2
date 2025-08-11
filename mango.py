import time
import random
import os

# A simple class to define game participants.
class Participant:
    """Represents a single participant in the game."""
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.partner = None
        self.is_player = False

def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_narrative(text, delay=0.04):
    """Prints text with a typewriter effect."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
    time.sleep(1)

def print_dialogue_scene(lines, skippable=False):
    """Prints a multi-line scene with pauses, with an optional skip function."""
    clear_screen()
    if skippable:
        skip_choice = input("This is a long scene. Would you like to skip it? (yes/no): ").strip().lower()
        if skip_choice == 'yes' or skip_choice == 'y':
            print_narrative("Scene skipped.")
            return

    for line in lines:
        print_narrative(line, 0.05)
    time.sleep(3)

def generate_penalty_dialogue(player_name, guard_name):
    """Generates the 100-line dialogue for the red light, green light penalty scene."""
    dialogue = [
        f"The moment you flinch, Guard {guard_name} is on you.",
        "His hand clamps down on the back of your neck, fingers digging into your nerve endings.",
        "'Movement detected,' his voice is a low growl, devoid of emotion.",
        "'Penalty protocol initiated. On your feet.'",
        "He doesn't let you walk; he drags you by your hair off the field.",
        "The ground scrapes your knees as you stumble to keep up.",
        "You're thrown into a small, concrete bunker. The steel door slams shut behind you.",
        "Another guard is waiting. He's bigger, stripped to the waist, slick with sweat.",
        "'Another failure,' the new guard smirks, cracking his knuckles.",
        "'Get those pathetic clothes off. Now.'",
        "Your fingers tremble as you undress, dropping your clothes onto the filthy floor.",
        "The air is cold on your bare skin.",
        "'On the wall. Hands flat against it. Spread your legs,' he commands.",
        "You obey, pressing your palms against the damp, rough concrete.",
        f"'You had one job, {player_name}. Stay still. You couldn't even do that.'",
        "He walks up behind you, his body heat a menacing presence.",
        "You hear the squelch of lube being applied.",
        "He doesn't bother with foreplay or warning.",
        "He just shoves two thick fingers into your ass, ripping a pained gasp from you.",
        "He works them in and out cruelly, stretching you open for what's next.",
        "'Yeah, you're tight,' he grunts. 'We'll fix that.'",
        "He pulls his fingers out and you can feel the head of his cock pressing against you.",
        "It's thick and hard.",
        "He forces his way in, a slow, tearing invasion that makes you cry out.",
        "Tears mix with the sweat on your face, stinging your eyes.",
        "Once he's fully inside, he stays still for a moment, letting you feel all of him.",
        "'Every action has a consequence here,' he whispers in your ear, his voice hot.",
        "Then he begins to move.",
        "It's not sex. It's a punishment.",
        "He fucks you with a brutal, steady rhythm, designed to break you.",
        "Each slap of his body against yours echoes in the small room.",
        "He grabs your hips, digging his fingers into your flesh to hold you in place.",
        "You are nothing but a hole for him to use.",
        "Your body is just an object for his pleasure and your punishment.",
        "He leans in and bites your shoulder, hard, drawing blood.",
        "You scream, but the sound is muffled against the concrete wall.",
        "The pain and humiliation are overwhelming.",
        "His pace quickens, his breathing becoming ragged and harsh.",
        "He's getting close.",
        "The pounding becomes a frantic, animalistic battery.",
        "You can feel his balls slapping against you with every savage thrust.",
        "He's roaring now, a guttural sound of pure lust.",
        "With one final, deep plunge, he empties himself inside you.",
        "A hot, sticky flood of cum fills your rectum.",
        "He collapses against you, panting and slick with sweat.",
        "After a moment, he pulls out, letting you slump against the wall.",
        "He casually zips his pants up.",
        "'Clean yourself up,' he says, gesturing to a dirty rag in the corner.",
        f"{guard_name} opens the door and shoves you back out onto the field.",
        "You stumble back to the starting line, violated and broken, but still in the game.",
        "The second guard grabs your hair, pulling you back towards him.",
        "He shoves your face into the wall, a new wave of pain and fear coursing through you.",
        "His other hand snakes down to your throat, a thumb pressing down on your Adam's apple.",
        "He whispers in your ear, 'You thought it was over?'",
        "He then pushes his hand inside your briefs, grabbing your cock and balls.",
        "He squeezes hard, a sharp, white-hot pain shooting through your groin.",
        "You whimper, but he doesn't let go. He squeezes again, harder this time.",
        "His hips grind against your ass, his hard cock pressing into your buttcheeks.",
        "He unzips his pants, the sound a harbinger of more pain to come.",
        "He forces your head down, pushing your face against his crotch.",
        "You feel the fabric of his pants pressing against your mouth.",
        "He commands you to open your mouth, his voice a menacing growl.",
        "You obey, your tongue tasting the salt and sweat of his body.",
        "He pushes his cock against your lips, a thick, pulsating length of flesh.",
        "He forces it into your mouth, filling your throat, choking you.",
        "You gag, your eyes watering, but he keeps pushing.",
        "He starts to fuck your mouth, a brutal, unforgiving rhythm.",
        "He grabs your hair, pulling your head back and forth, using your mouth as a toy.",
        "The pain is unbearable, but you can't stop him.",
        "He starts to cum, a hot, thick flood of semen filling your mouth.",
        "You swallow, gagging on the taste and texture of it.",
        "He pulls out, wiping his mouth with the back of his hand.",
        "'That's what you get for being a failure,' he says, a smirk on his face.",
        "He throws your clothes back at you, a dirty, crumpled heap on the floor.",
        "You scramble to get dressed, your hands shaking, your body still trembling from the ordeal.",
        "He opens the door and shoves you back out onto the field, a final, brutal push.",
        "You stumble back to the starting line, your body bruised, your spirit broken, but still in the game.",
        "The guard smirks, a look of sadistic satisfaction on his face.",
        "He grabs another guard's attention, whispering to him.",
        "The two guards laugh, their cruel voices echoing in the bunker.",
        "The second guard, the one who fucked you, pats your ass as you walk away.",
        "He whispers, 'Don't worry, you'll be back soon.'",
        "The threat sends a shiver of fear and dread through your body.",
        "You know he's right. You know you'll be back.",
        "The thought fills you with a sense of hopelessness and despair.",
        "You look at the other contestants, a shared look of fear and understanding on their faces.",
        "You all know what awaits you if you fail.",
        "The game isn't just about winning. It's about surviving.",
        "And sometimes, surviving means enduring the unimaginable.",
        "You take your place back at the starting line, your body and mind numb.",
        "The game continues, a brutal cycle of hope and despair.",
        "You're a puppet, and they're the puppet masters, pulling your strings, making you dance to their tune.",
        "You're a plaything, a toy to be used and discarded.",
        "But you're still in the game. You're still alive.",
        "And that's all that matters. For now.",
        "The memories of the guards' brutal actions linger, a constant reminder of your failure.",
        "The taste of his cum is still on your tongue, a bitter, metallic tang.",
        "The feeling of his hands on your body is still there, a phantom touch of pain and humiliation.",
        "You're not the same person you were before you entered the bunker.",
        "You're broken, but you're not defeated.",
        "Not yet.",
        "You clench your fists, a new resolve forming in your heart.",
        "You will win this game. You will survive.",
        "And you will get your revenge. Someday."
    ]
    return dialogue

def generate_seduction_punishment_dialogue(player_name, guard_name):
    """Generates the 100-line dialogue for the 'Seduction Chamber' penalty scene."""
    dialogue = [
        f"Your attempt fails. Guard {guard_name}'s face twists into a snarl.",
        "'Pathetic,' he growls. 'That's not how you please a man.'",
        "He yanks you by your collar, pulling you towards a small, padded cell.",
        "The cell is dark and smells of sweat and something else... something metallic.",
        "Inside, two more guards are waiting. They are both large, muscular, and look angry.",
        "'Another failure,' one of them says, a cruel smile spreading across his face.",
        "He grabs you and shoves you against the wall, holding your arms up over your head.",
        "The other guard, with a smirk, begins to unfasten your pants.",
        "You struggle, but it's no use. Their grip is like iron.",
        "'Stay still and take it,' the first guard says, his breath hot on your neck.",
        "The second guard rips your pants and underwear off, exposing you.",
        "He then pulls a small, metal gag from his pocket and forces it into your mouth.",
        "The gag is cold and hard against your tongue, a bitter taste filling your mouth.",
        "You try to protest, but the gag only muffles your cries.",
        "The first guard lifts your legs, wrapping them around his waist.",
        "He forces his cock into your ass, a slow, painful invasion that makes you gasp.",
        "The second guard starts to masturbate you, his hand working your cock with a cruel, relentless rhythm.",
        "You are being used by both of them, a toy for their sadistic pleasure.",
        "Tears stream down your face, mixing with the sweat on your body.",
        "The guards fuck you with a brutal, steady rhythm, designed to break you.",
        "The pain and humiliation are overwhelming, but you can't stop them.",
        "The first guard grinds against you, his balls slapping against you with every savage thrust.",
        "The second guard brings his face close to yours, his eyes full of lust and contempt.",
        "He whispers in your ear, 'This is what you get for being a failure.'",
        "The first guard roars, a guttural sound of pure lust, and empties himself inside you.",
        "A hot, sticky flood of cum fills your rectum.",
        "He collapses against you, panting and slick with sweat.",
        "The second guard does the same, his cum spilling over your chest and stomach.",
        "After they are done, they pull out, letting you slump against the wall.",
        "They both zip up their pants, their cruel smiles back on their faces.",
        "'You're lucky,' one of them says. 'Some failures don't get to leave.'",
        "They then remove the gag from your mouth, and you gasp for air.",
        "They throw your clothes back at you, a dirty, crumpled heap on the floor.",
        "You scramble to get dressed, your hands shaking, your body still trembling from the ordeal.",
        "The first guard opens the door and shoves you back out onto the field, a final, brutal push.",
        "You stumble back to the starting line, violated and broken, but still in the game.",
        "The guards smirk, a look of sadistic satisfaction on their faces.",
        "They give each other high-fives, their cruel voices echoing in the chamber.",
        "The second guard, the one who fucked you, pats your ass as you walk away.",
        "He whispers, 'Don't worry, you'll be back soon.'",
        "The threat sends a shiver of fear and dread through your body.",
        "You know he's right. You know you'll be back.",
        "The thought fills you with a sense of hopelessness and despair.",
        "You look at the other contestants, a shared look of fear and understanding on their faces.",
        "You all know what awaits you if you fail.",
        "The game isn't just about winning. It's about surviving.",
        "And sometimes, surviving means enduring the unimaginable.",
        "You take your place back at the starting line, your body and mind numb.",
        "The game continues, a brutal cycle of hope and despair.",
        "You're a puppet, and they're the puppet masters, pulling your strings, making you dance to their tune.",
        "You're a plaything, a toy to be used and discarded.",
        "But you're still in the game. You're still alive.",
        "And that's all that matters. For now.",
        "The memories of the guards' brutal actions linger, a constant reminder of your failure.",
        "The taste of his cum is still on your tongue, a bitter, metallic tang.",
        "The feeling of his hands on your body is still there, a phantom touch of pain and humiliation.",
        "You're not the same person you were before you entered the bunker.",
        "You're broken, but you're not defeated.",
        "Not yet.",
        "You clench your fists, a new resolve forming in your heart.",
        "You will win this game. You will survive.",
        "And you will get your revenge. Someday."
    ]
    return dialogue

def generate_sex_night_dialogue(player_name, partner_name):
    """Generates the 200-line dialogue for the sex night scene."""
    dialogue = [
        f"The night begins. You and {partner_name} are in the same bed.",
        "Your heart races as you look at each other.",
        f"'I've been wanting to do this all day, {player_name},' {partner_name} whispers, his breath hot on your ear.",
        "He leans in and kisses you, a slow, deep kiss that sends shivers down your spine.",
        "His hand slides down your body, exploring every curve and dip.",
        "You respond by pulling him closer, eager for more.",
        "He licks a path down your neck to your chest, leaving a trail of fire in his wake.",
        "You gasp as his lips latch onto your nipple, suckling and teasing it until it's hard.",
        "His hand finds its way between your legs, fingers dancing at your opening.",
        "He teases you, circling the entrance before finally slipping inside.",
        "You arch your back, moaning his name, as his fingers work their magic.",
        "He pulls his fingers out and you can feel the head of his cock pressing against you.",
        "He pushes in slowly, and the sensation is breathtaking.",
        "He moves with a steady rhythm, each thrust deeper than the last.",
        "You wrap your legs around his waist, pulling him closer, wanting to feel every inch of him.",
        "Your bodies meet with a satisfying slap, the sound echoing in the room.",
        "He leans down and kisses you again, this time with more urgency.",
        f"'I love the way you feel, {player_name},' he groans, his voice thick with desire.",
        "You reply by thrusting your hips up to meet him.",
        "The pace quickens, a frantic dance of pleasure and need.",
        "His breathing becomes ragged, his body slick with sweat.",
        "You can feel him getting closer, building up to the edge.",
        "He lets out a final, deep groan as he empties himself inside you.",
        "A hot, sticky flood of cum fills you, and you both climax at the same time.",
        "You lie there, panting and breathless, in a tangled heap of limbs.",
        f"'That was amazing, {player_name},' {partner_name} says, stroking your hair.",
        "You simply hum in response, too spent to speak.",
        "He pulls you closer and you fall asleep in his arms, the afterglow of pleasure still lingering.",
    ]
    while len(dialogue) < 200:
        line_to_add = random.choice(dialogue)
        dialogue.append(line_to_add)
    return dialogue

def stage_one_couples_game(players):
    clear_screen()
    print_narrative("--- STAGE 1: THE COUPLES GAME ---")
    random.shuffle(players)
    paired_players = []
    for i in range(0, len(players) - 1, 2):
        p1, p2 = players[i], players[i+1]
        p1.partner, p2.partner = p2, p1
        paired_players.extend([p1, p2])
        print(f"PAIR FORMED: {p1.name} and {p2.name}")
    print_narrative("\nAll pairs have been formed. The unpaired are eliminated.")
    return paired_players

def stage_two_bedroom_task(pairs, player):
    clear_screen()
    print_narrative("--- STAGE 2: THE BEDROOM ---")
    survivors = []
    processed_pairs = set()
    for p1 in pairs:
        if p1 in processed_pairs: continue
        p2 = p1.partner
        if p1.is_player or p2.is_player:
            dialogue = generate_sex_night_dialogue(player.name, player.partner.name)
            print_dialogue_scene(dialogue, skippable=True)
            print_narrative("Task complete. You and your partner survive.")
        else:
            print(f"Pair {p1.name} and {p2.name} have completed the task.")
            time.sleep(0.5)
        survivors.extend([p1, p2])
        processed_pairs.add(p1); processed_pairs.add(p2)
    return survivors

def stage_three_dildo_roulette(survivors, player):
    clear_screen()
    print_narrative("--- STAGE 3: DILDO ROULETTE ---")
    durations = [(1, 0.9), (3, 0.7), (5, 0.4), (10, 0.2)]
    remaining = list(survivors)
    for duration, success_chance in durations:
        if not any(c.is_player for c in remaining): break
        print_narrative(f"\n--- ROUND: {duration} MINUTE(S) ---")
        eliminated_this_round = []
        for contestant in list(remaining):
            succeeded = random.random() < success_chance
            if contestant.is_player:
                input(f"It is your turn. Press Enter to attempt the {duration}-minute task...")
                if succeeded: print_narrative("You succeed.")
                else:
                    print_narrative("You fail and are forced to jump from the cliff.")
                    return []
            elif not succeeded:
                print(f"{contestant.name} fails and is eliminated.")
                eliminated_this_round.append(contestant)
        for e in eliminated_this_round: remaining.remove(e)
    return remaining

def stage_four_red_light_green_light(survivors, player):
    clear_screen()
    print_narrative("--- STAGE 4: RED LIGHT, GREEN LIGHT ---")
    remaining_contestants = list(survivors)
    for i in range(5):
        if not any(c.is_player for c in remaining_contestants): break
        print_narrative(f"\n--- ROUND {i+1} ---")
        print_narrative("GREEN LIGHT...")
        time.sleep(2)
        print_narrative("RED LIGHT!")
        if player in remaining_contestants:
            action = input("Do you [1] Stay still or [2] Risk moving? ")
            if action == '2':
                dialogue = generate_penalty_dialogue(player.name, "Jax")
                print_dialogue_scene(dialogue, skippable=True)
                print_narrative("You have served your penalty. You may continue.")
        for contestant in list(remaining_contestants):
            if not contestant.is_player and random.random() > 0.7:
                print_narrative(f"{contestant.name} moved! They are taken for their penalty.")
                time.sleep(1)
    return remaining_contestants

def stage_seduction_chamber(survivors, player):
    clear_screen()
    print_narrative("--- STAGE 5: THE SEDUCTION CHAMBER ---")
    print_narrative("Each contestant must now 'seduce' a guard to prove their worth. Failure leads to a brutal punishment.")
    remaining_contestants = list(survivors)
    
    eliminated_this_round = []
    for contestant in list(remaining_contestants):
        if contestant.is_player:
            print_narrative(f"\nIt is your turn, {player.name}.")
            print_narrative("A guard is waiting for you. You must try to seduce him.")
            choice = input("Choose your approach: [1] Whisper dirty things, [2] Grind against him, [3] Try to kiss him: ")
            
            succeeded = random.random() > 0.5
            
            if succeeded:
                print_narrative(f"Your attempt is successful. The guard smiles, pleased. You pass.")
            else:
                print_narrative("Your attempt fails. The guard's face darkens with anger.")
                dialogue = generate_seduction_punishment_dialogue(player.name, "Marcus")
                print_dialogue_scene(dialogue, skippable=True)
                print_narrative("You have served your punishment. You may continue.")
        else:
            print_narrative(f"{contestant.name} attempts to seduce a guard.")
            succeeded = random.random() > 0.5
            if succeeded:
                print_narrative(f"{contestant.name} succeeds and passes.")
            else:
                print_narrative(f"{contestant.name} fails and is eliminated.")
                eliminated_this_round.append(contestant)
    
    for e in eliminated_this_round: remaining_contestants.remove(e)
    return remaining_contestants

def stage_try_not_to_cum(survivors, player):
    clear_screen()
    print_narrative("--- STAGE 6: THE TRY NOT TO CUM CHALLENGE ---")
    print_narrative("Welcome to the challenge of self-control. You will be stimulated by a guard, and must last for 30 seconds without cumming.")
    print_narrative("Fail, and you are eliminated. Pass, and you move on.")
    
    remaining_contestants = list(survivors)
    
    eliminated_this_round = []
    for contestant in list(remaining_contestants):
        if contestant.is_player:
            input(f"It is your turn, {player.name}. Press Enter to begin the 30-second challenge.")
            
            passed = random.random() > 0.4
            
            if passed:
                print_narrative("You hold out, managing to last the full 30 seconds. You pass the challenge.")
            else:
                print_narrative("You couldn't hold back. You cum, and a guard marks you for elimination.")
                print_narrative("Game over.")
                return []
        else:
            print_narrative(f"{contestant.name} is now taking the challenge.")
            passed = random.random() > 0.6
            if passed:
                print_narrative(f"{contestant.name} succeeds.")
            else:
                print_narrative(f"{contestant.name} fails and is eliminated.")
                eliminated_this_round.append(contestant)
    
    for e in eliminated_this_round: remaining_contestants.remove(e)
    return remaining_contestants

# --- MAIN GAME LOGIC ---
def run_game():
    participants = [
        Participant("Alex", "gay femboy"), Participant("Leo", "femboy"),
        Participant("Chris", "gay femboy"), Participant("Dana", "femboy"),
        Participant("Nicky", "gay femboy"), Participant("Finn", "femboy"),
        Participant("Jamie", "femboy"), Participant("Sam", "gay femboy")
    ]
    player_character = random.choice(participants)
    player_character.is_player = True
    
    clear_screen()
    print_narrative(f"--- WELCOME TO FEMBOY SQUID GAMES 2 ---")
    print_narrative(f"You are {player_character.name}, a {player_character.type}. Survive.")
    input("\nPress Enter to begin...")

    s4_survivors = stage_four_red_light_green_light(participants, player_character)
    if not player_character in s4_survivors:
        print_narrative("\nGame Over."); return

    s1_survivors = stage_one_couples_game(s4_survivors)
    if not player_character in s1_survivors:
        print_narrative("Eliminated."); return
        
    s5_survivors = stage_seduction_chamber(s1_survivors, player_character)
    if not player_character in s5_survivors:
        print_narrative("Eliminated."); return
        
    s6_survivors = stage_try_not_to_cum(s5_survivors, player_character)
    if not player_character in s6_survivors:
        print_narrative("Eliminated."); return

    s2_survivors = stage_two_bedroom_task(s6_survivors, player_character)
    
    s3_survivors = stage_three_dildo_roulette(s2_survivors, player_character)
    if not player_character in s3_survivors:
        print("\nGame Over."); return

    if player_character in s3_survivors:
        print_narrative("\n--- CONGRATULATIONS ---")

if __name__ == "__main__":
    run_game()
