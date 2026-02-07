# PropModCreator

A GUI tool for creating Project Zomboid mods without coding.

Create professional profession and trait mods for Project Zomboid Build 42 with an easy-to-use graphical interface. No programming knowledge required.

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-yellow)

## What It Does

PropModCreator lets you create Project Zomboid profession and trait mods through a simple point-and-click interface. Generated mods use PropFramework (available on Steam Workshop) and are ready to upload to Steam Workshop or share with friends.

## Features

- No Coding Required - Point and click interface
- Profession Creator - Skills, traits, starting items
- Trait Creator - Custom traits with point costs
- Project Management - Save and load projects
- Automatic Generation - Creates all mod files
- PropFramework Integration - Automatic dependency

## Requirements

- Python 3.8 or higher
- PropFramework (for generated mods, available on Steam Workshop)
- Project Zomboid Build 42

## Installation

### Windows

1. Install Python from python.org
   - Check "Add Python to PATH" during installation

2. Download PropModCreator
   ```bash
   git clone https://github.com/prop11/propFramework.git
   cd PropModCreator
   ```

3. Install Dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Run
   ```bash
   python prop_mod_creator.py
   ```
   Or double-click run.bat

### Linux

1. Install Python
   ```bash
   sudo apt-get update
   sudo apt-get install python3 python3-pip python3-tk
   ```

2. Download and Install
   ```bash
   git clone https://github.com/prop11/propFramework.git
   cd PropModCreator
   pip3 install -r requirements.txt
   python3 prop_mod_creator.py
   ```
   Or run ./run.sh

### Mac

1. Install Python
   ```bash
   brew install python@3.12
   ```

2. Download and Install
   ```bash
   git clone https://github.com/prop11/propFramework.git
   cd PropModCreator
   pip3 install -r requirements.txt
   python3 prop_mod_creator.py
   ```
   Or run ./run.sh

## Quick Start

1. Fill in Mod Info tab (name, ID, author, description)
2. Create Professions (add skills, traits, items)
3. Create Traits (optional)
4. Generate Mod (File menu)
5. Upload to Steam Workshop or copy to mods folder

See QUICKSTART.md for detailed 5-minute guide.
See TUTORIAL.md for step-by-step walkthrough.

## Creating a Profession

1. Click Professions tab
2. Click Add Profession
3. Fill in details:
   - Name (e.g., "Mechanic")
   - Point Cost (e.g., 6)
   - Description
4. Add Skills (select from dropdown, set level)
5. Add Traits (select from dropdown)
6. Add Starting Items (item type + count)
7. Save Profession

## Available Skills

Crafting: Carpentry, Woodwork, Metalworking, Tailoring, Mechanics, Electricity
Survival: Farming, Fishing, Trapping, Foraging, Cooking, FirstAid
Combat: Aiming, Reloading, Axe, Blunt, LongBlade, SmallBlade, Spear
Physical: Fitness, Strength, Sprinting, Lightfooted, Nimble, Sneak

## Common Item Types

Tools: Base.Hammer, Base.Saw, Base.Screwdriver, Base.Wrench, Base.Axe
Weapons: Base.HandAxe, Base.BaseballBat, Base.KitchenKnife
Food: Base.CannedBeans, Base.WaterBottle
Medical: Base.Bandage, Base.Pills, Base.FirstAidKit
Materials: Base.Nails, Base.Plank, Base.ScrapMetal

## Generating Mods

1. File → Generate Mod
2. Select output directory (your Zomboid/mods folder or desktop)
3. Generated folder structure:
   ```
   YourModName/
   ├── mod.info
   ├── README.md
   └── media/lua/shared/
       └── YourModName.lua
   ```

## Installing Generated Mods

### Steam Workshop (Recommended)

1. Open Steam Workshop for Project Zomboid
2. Click "Upload Item" or use Steamworks SDK
3. Add your mod folder
4. Set PropFramework as required item
5. Upload

### Manual Installation

1. Make sure PropFramework is installed (subscribe on Steam Workshop)
2. Copy generated mod folder to Zomboid/mods/
3. Enable both PropFramework and your mod in-game
4. Start new game and select your profession

## Project Files

Save your work as JSON:
- File → Save Project
- File → Load Project

Projects can be shared with others or used as templates.

## Example Projects

examples/example_project.json contains:
- 5 professions (Survivalist, Mechanic, Paramedic, Chef, Athlete)
- 3 traits

Load this to see how projects are structured.

## Troubleshooting

### Python Module Errors
```bash
pip install --upgrade -r requirements.txt
```

### Tkinter Not Found (Linux)
```bash
sudo apt-get install python3-tk
```

### Generated Mod Not Working
- Check PropFramework is enabled in-game
- Check console (F11) for errors
- Verify mod files were generated correctly
- Make sure both mods are enabled

## Tips for Good Mods

Balance:
- 2-8 points for most professions
- 1-3 starting levels per skill
- Realistic starting items

Design:
- Focus on a theme
- Group related skills
- Match traits to background
- Write clear descriptions

Testing:
- Test with different game modes
- Check if too strong/weak
- Get feedback from players

## Documentation

- README.md - This file
- QUICKSTART.md - 5-minute getting started
- TUTORIAL.md - Step-by-step walkthrough
- PROJECT_OVERVIEW.md - Technical details
- CONTRIBUTING.md - Developer guide

## Workflow

For content creators:
1. Design profession concept
2. Use PropModCreator to create it
3. Generate mod files
4. Test in-game
5. Upload to Steam Workshop

For players:
1. Subscribe to PropFramework on Steam Workshop
2. Subscribe to mods that use it
3. Play

## Future Features

Planned:
- Custom item creation
- Recipe creator
- Visual profession icons
- Mod preview
- Templates library

## Support

- GitHub Issues - Bug reports and features
- GitHub Discussions - Questions and help
- Project Zomboid Discord - Community support

## Contributing

Contributions welcome:
1. Fork repository
2. Create feature branch
3. Make changes
4. Submit pull request

See CONTRIBUTING.md for guidelines.

## License

MIT License - Free to use and modify

## Credits

Created for the Project Zomboid modding community
Uses PropFramework for mod functionality
Built with Python and Tkinter

## Version History

1.0.0 - Initial release
- Profession creator
- Trait creator
- Project management
- Mod generation
- PropFramework integration

## FAQ

Q: Do I need to know programming?
A: No, PropModCreator handles all code generation.

Q: Can I edit generated files?
A: Yes, the Lua code is clean and well-structured.

Q: Will this work in multiplayer?
A: Yes, if all players have PropFramework and your mod.

Q: Can I share my mods?
A: Yes, upload to Steam Workshop or share files directly.

Q: What if I want features not in the GUI?
A: Generate a basic mod, then manually edit the Lua files.

## Steam Workshop Integration

Generated mods are ready for Steam Workshop:
1. Include PropFramework as required item
2. Mention PropFramework in description
3. Test thoroughly before uploading
4. Update version numbers for releases

PropFramework handles all the framework code, so your mods are clean and simple.
