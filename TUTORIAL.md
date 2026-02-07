# Step-by-Step Tutorial - Creating Your First Mod

# Tutorial: Creating a "Forest Ranger" Profession

This tutorial walks you through creating your first mod from start to finish.

---

# Part 1: Setup (First Time Only)

# Windows Users
```bash
1. Download Python from python.org
2. Install Python (check "Add to PATH")
3. Download PropModCreator
4. Open Command Prompt in PropModCreator folder
5. Run: pip install -r requirements.txt
6. Double-click run.bat
```

# Linux/Mac Users
```bash
1. Open Terminal
2. cd to PropModCreator folder
3. Run: pip3 install -r requirements.txt
4. Run: ./run.sh
```

 Checkpoint: PropModCreator window should open

---

# Part 2: Mod Information

# Step 1: Open Mod Info Tab
- The "Mod Info" tab should be selected by default
- This is where we set up basic mod details

# Step 2: Fill in Details
```
Mod Name: Forest Ranger Pack
Mod ID: ForestRangerPack
Author: [Your Name]
Version: 1.0.0
Description: Adds the Forest Ranger profession - an expert in wilderness survival, tracking, and forest management.
```

Important: Mod ID must have NO SPACES!

 Checkpoint: All fields filled in

---

# Part 3: Creating the Profession

# Step 1: Go to Professions Tab
- Click on "Professions" tab at the top

# Step 2: Click "Add Profession"
- A dialog window will open

# Step 3: Basic Information
Fill in these fields:
```
Profession Name: Forest Ranger
Point Cost: 5
Description: A professional forest ranger skilled in outdoor survival, wildlife management, and emergency response.
```

Why 5 points?
- We're giving them 5 skills
- Plus useful traits
- This makes them moderately expensive

# Step 4: Add Skills

Click in the Skills section and add these one by one:

| Skill | Level | How to Add |
|-------|-------|------------|
| Foraging | 3 | Select "Foraging", set 3, click "Add Skill" |
| Trapping | 2 | Select "Trapping", set 2, click "Add Skill" |
| Fishing | 2 | Select "Fishing", set 2, click "Add Skill" |
| Fitness | 2 | Select "Fitness", set 2, click "Add Skill" |
| FirstAid | 1 | Select "FirstAid", set 1, click "Add Skill" |

Skill Reasoning:
- Foraging (3): Primary skill for finding food in forests
- Trapping (2): Important for sustainable food
- Fishing (2): Alternative food source
- Fitness (2): Rangers are physically active
- FirstAid (1): Basic emergency training

# Step 5: Add Traits

In the Traits section:
1. Select "Outdoorsman" from dropdown
2. Click "Add Trait"
3. Select "Keen Hearing" from dropdown
4. Click "Add Trait"

Trait Reasoning:
- Outdoorsman: Obvious fit for forest ranger
- Keen Hearing: Useful for tracking and safety

# Step 6: Add Starting Items

In the Starting Items section, add these:

| Item Type | Count | Notes |
|-----------|-------|-------|
| Base.HuntingKnife | 1 | Essential tool |
| Base.Rope | 2 | For various uses |
| Base.WaterBottle | 1 | Hydration |
| Base.Matches | 1 | Fire starting |
| Base.Bandage | 3 | First aid |

To add each item:
1. Type the item type (e.g., "Base.HuntingKnife")
2. Set count
3. Click "Add Item"

# Step 7: Save the Profession
- Review everything in the dialog
- Click "Save Profession"
- You should see "Forest Ranger" in the list on the left

 Checkpoint: Forest Ranger appears in profession list

---

# Part 4: (Optional) Adding a Custom Trait

Let's add a custom trait to demonstrate the system.

# Step 1: Go to Traits Tab
- Click on "Traits" tab

# Step 2: Click "Add Trait"
- A simpler dialog will open

# Step 3: Fill in Trait Details
```
Trait Name: ForestWise
Point Cost: -4
Description: Years in the forest have sharpened your senses and instincts. You can identify edible plants more easily and spot wildlife before they spot you.
```

Why -4 points?
- Negative cost means it costs the player points
- It's a positive trait (beneficial)
- -4 is moderate for a profession-specific trait

# Step 4: Save Trait
- Click "Save Trait"
- You should see "ForestWise" in the trait list

 Checkpoint: Custom trait created

---

# Part 5: Generating the Mod

# Step 1: Save Your Project (Recommended)
```
File → Save Project
Name: ForestRanger.json
Location: Anywhere you want to keep project files
```

Why save the project?
- You can edit it later
- You can share it with others
- Backup before generation

# Step 2: Generate the Mod
```
File → Generate Mod
```

# Step 3: Choose Output Location
Option A - Direct Install:
- Navigate to: `C:\Users\[YourName]\Zomboid\mods\`
- Click "Select Folder"

Option B - Desktop First:
- Select Desktop or Downloads
- You'll copy it later

# Step 4: Generation Complete
You should see a success message:
```
Mod generated successfully!
Location: [path]/ForestRangerPack
```

 Checkpoint: Mod files created

---

# Part 6: Verify Generated Files

# Navigate to Generated Folder
Open the folder in File Explorer/Finder:
```
ForestRangerPack/
 mod.info
 README.md
 media/
     lua/
         shared/
             ForestRangerPack.lua
```

# Check mod.info
Should contain:
- name=Forest Ranger Pack
- id=ForestRangerPack
- require=PropFramework

# Check .lua File
Open ForestRangerPack.lua - you should see:
- PropFramework imports
- Profession registration
- Skills, traits, items configured

 Checkpoint: All files present and correct

---

# Part 7: Installing in Project Zomboid

# Step 1: Install PropFramework
If you haven't already:
1. Download PropFramework
2. Copy to `Zomboid/mods/PropFramework`

# Step 2: Install Your Mod
Copy `ForestRangerPack` folder to:
- Windows: `C:\Users\[YourName]\Zomboid\mods\`
- Linux: `~/.zomboid/mods/`
- Mac: `~/Library/Application Support/Zomboid/mods/`

# Step 3: Enable Mods
1. Launch Project Zomboid
2. Main Menu → Mods
3. Check both:
   -  PropFramework
   -  Forest Ranger Pack
4. Click "Accept" or "OK"

 Checkpoint: Both mods enabled

---

# Part 8: Testing Your Profession

# Step 1: Start New Game
- Main Menu → Solo
- Choose your game mode
- Click "Next"

# Step 2: Character Creation
- At profession selection screen
- Look for "Forest Ranger" in the list
- Select it

# Step 3: Verify Skills
Check that you have:
- Foraging (3 stars)
- Trapping (2 stars)
- Fishing (2 stars)
- Fitness (2 stars)
- FirstAid (1 star)

# Step 4: Verify Traits
Should have:
- Outdoorsman
- Keen Hearing

# Step 5: Check Starting Items
Press "I" for inventory:
- Hunting Knife
- Rope (2)
- Water Bottle
- Matches
- Bandage (3)

 Checkpoint: Everything works!

---

# Part 9: What Next?

# Enhance Your Mod
- Add more professions (Park Ranger, Wildlife Biologist)
- Create complementary traits
- Add recipes (future feature)
- Adjust balance based on testing

# Share Your Mod
1. Test thoroughly
2. Write better description in README
3. Upload to Steam Workshop
4. Share on Project Zomboid forums
5. Credit PropFramework!

# Create More Mods
Try these ideas:
- Military professions pack
- Medical professions pack
- Criminal backgrounds pack
- Apocalypse survivor pack

---

# Troubleshooting Common Issues

# Mod Not Appearing in Game
Solution:
1. Check mod is in correct folder
2. Verify mod.info exists
3. Restart game completely
4. Re-enable in mod menu

# Profession Not in List
Solution:
1. Enable PropFramework first
2. Check console (F11) for errors
3. Verify .lua file has no syntax errors
4. Make sure both mods are enabled

# Starting Items Not Appearing
Solution:
1. Check item types are correct (Base.ItemName)
2. Common mistake: "Base.Knife" vs "Base.HuntingKnife"
3. Refer to PropFramework docs for item names

# Skills Not Applied
Solution:
1. Verify skill names match exactly
2. Check console for errors
3. Make sure profession is actually selected

---

# Tips for Success

# Balance Tips
 Good: 5 points for 5 skills (level 1-3 each)
 Bad: 2 points for 10 skills (all level 10)

 Good: Themed starting items
 Bad: Shotgun, 1000 ammo, military gear

 Good: 2-3 relevant traits
 Bad: Every positive trait possible

# Design Tips
- Focus on a theme (forest ranger, mechanic, doctor)
- Skills should support each other
- Traits should match profession background
- Starting items should be realistic
- Description should explain the profession clearly

# Testing Tips
- Test with different game modes
- Try different character builds
- Check if it's too strong/weak
- Get feedback from friends
- Adjust and regenerate

---

# Congratulations!

You've created your first Project Zomboid mod!

# What You Learned
 Installing PropModCreator
 Setting up mod information
 Creating professions with skills/traits/items
 Generating mod files
 Installing and testing mods

# Next Steps
1. Create more professions
2. Experiment with trait combinations
3. Share your creations
4. Join the modding community

Happy Modding!

---

# Quick Reference Card

```
Installation: pip install -r requirements.txt
Run: python prop_mod_creator.py
Mod Folder: Zomboid/mods/
Enable: Main Menu → Mods
Test: Create New Character
Console: F11 (for errors)

Good Point Costs:
- Simple: 2-4 points
- Moderate: 4-6 points
- Complex: 6-8 points
- Expert: 8-10 points

Skill Levels:
- Beginner: 1-2
- Intermediate: 3-4
- Advanced: 5-7
- Expert: 8-10
```
