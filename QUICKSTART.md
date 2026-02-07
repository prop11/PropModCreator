# Quick Start Guide - PropModCreator

# 5-Minute Setup

# Step 1: Install (2 minutes)
```bash
# Install Python from python.org if not installed

# Install PropModCreator
pip install -r requirements.txt
```

# Step 2: Run (30 seconds)
```bash
python prop_mod_creator.py
```

# Step 3: Create Your First Mod (2 minutes)

# A. Fill Mod Info
1. Mod Name: `My First Mod`
2. Mod ID: `MyFirstMod` (no spaces!)
3. Author: Your name
4. Description: What your mod does

# B. Create a Profession
1. Click "Professions" tab
2. Click "Add Profession"
3. Fill in:
   - Name: `Carpenter`
   - Cost: `4`
   - Description: `Skilled woodworker`
4. Add Skills:
   - Carpentry: 3
   - Woodwork: 2
5. Add Trait:
   - Select `Handy`
6. Add Items:
   - `Base.Hammer` x 1
   - `Base.Saw` x 1
   - `Base.Nails` x 50
7. Click "Save Profession"

# C. Generate
1. Menu: File → Generate Mod
2. Choose your `Zomboid/mods/` folder
3. Done!

# Step 4: Install & Play (30 seconds)
1. Make sure PropFramework is in `Zomboid/mods/`
2. Enable both mods in-game
3. Start new game
4. Select your profession!

# Common Examples

# Hunter
```
Skills: Aiming (3), Trapping (2), Foraging (1)
Traits: Outdoorsman, Keen Hearing
Items: Shotgun, Shells (10), Hunting Knife
Cost: 6 points
```

# Mechanic
```
Skills: Mechanics (4), Metalworking (2), Electricity (1)
Traits: Handy
Items: Wrench, Screwdriver, Lug Wrench
Cost: 6 points
```

# Doctor
```
Skills: FirstAid (5), Fitness (1)
Traits: FastHealer, Resilient
Items: FirstAidKit, Pills (5), Bandage (10)
Cost: 8 points
```

# Chef
```
Skills: Cooking (4), Fishing (1), Foraging (1)
Traits: LightEater
Items: Frying Pan, Kitchen Knife, Pot
Cost: 4 points
```

# Tips

 Start Simple - One profession with 2-3 skills
 Test Often - Generate and test after each change
 Balance Costs - 4-6 points is typical for professions
 Save Projects - Use File → Save Project to preserve work
 Read Tooltips - Hover over fields for help

# Troubleshooting

App won't start?
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Can't find generated mod?
- Check the output directory you selected
- Look for folder named [YourModID]

Mod not working in-game?
- PropFramework must be installed first
- Enable both mods in mod menu
- Check console (F11) for errors

# Next Steps

1.  Create more complex professions
2.  Add custom traits
3.  Save project files for later
4.  Share your mods with the community!

# Need Help?

- Check README.md for full documentation
- See examples folder for inspiration
- Visit Project Zomboid modding Discord

---

You're ready to create awesome mods!
