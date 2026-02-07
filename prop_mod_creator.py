#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk, messagebox, filedialog, scrolledtext
import json
import os
from pathlib import Path
from datetime import datetime

class PropModCreator:
    def __init__(self, root):
        self.root = root
        self.root.title("PropModCreator - Project Zomboid Mod Generator")
        self.root.geometry("1000x700")
        
        self.mod_data = {
            "mod_name": "",
            "mod_id": "",
            "author": "",
            "description": "",
            "professions": [],
            "traits": [],
            "items": [],
            "recipes": []
        }
        
        self.setup_ui()
        
    def setup_ui(self):
        
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New Project", command=self.new_project)
        file_menu.add_command(label="Load Project", command=self.load_project)
        file_menu.add_command(label="Save Project", command=self.save_project)
        file_menu.add_separator()
        file_menu.add_command(label="Generate Mod", command=self.generate_mod)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)
        help_menu.add_command(label="Documentation", command=self.show_docs)
        
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(1, weight=1)
        
        title = ttk.Label(main_frame, text="PropModCreator", font=("Arial", 20, "bold"))
        title.grid(row=0, column=0, columnspan=2, pady=10)
        
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        
        self.create_mod_info_tab()
        self.create_professions_tab()
        self.create_traits_tab()
        self.create_items_tab()
        self.create_recipes_tab()
        
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, relief=tk.SUNKEN)
        status_bar.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
    def create_mod_info_tab(self):
        
        tab = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(tab, text="Mod Info")
        
        ttk.Label(tab, text="Mod Name:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.mod_name_entry = ttk.Entry(tab, width=40)
        self.mod_name_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)
        
        ttk.Label(tab, text="Mod ID:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.mod_id_entry = ttk.Entry(tab, width=40)
        self.mod_id_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)
        ttk.Label(tab, text="(No spaces, e.g., MyAwesomeMod)", font=("Arial", 8)).grid(row=1, column=2, sticky=tk.W)
        
        ttk.Label(tab, text="Author:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.author_entry = ttk.Entry(tab, width=40)
        self.author_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)
        
        ttk.Label(tab, text="Description:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.description_text = tk.Text(tab, height=5, width=40)
        self.description_text.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)
        
        ttk.Label(tab, text="Version:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.version_entry = ttk.Entry(tab, width=40)
        self.version_entry.insert(0, "1.0.0")
        self.version_entry.grid(row=4, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)
        
        info_frame = ttk.LabelFrame(tab, text="Requirements", padding="10")
        info_frame.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=20)
        
        ttk.Label(info_frame, text="✓ PropFramework (automatically added as dependency)", 
                 foreground="green").pack(anchor=tk.W)
        ttk.Label(info_frame, text="✓ Project Zomboid Build 42", 
                 foreground="green").pack(anchor=tk.W)
        
        tab.columnconfigure(1, weight=1)
        
    def create_professions_tab(self):
        
        tab = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(tab, text="Professions")
        
        left_frame = ttk.Frame(tab)
        left_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5)
        
        ttk.Label(left_frame, text="Professions:", font=("Arial", 12, "bold")).pack(anchor=tk.W)
        
        list_frame = ttk.Frame(left_frame)
        list_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        scrollbar = ttk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.profession_listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set, height=20)
        self.profession_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.profession_listbox.bind('<<ListboxSelect>>', self.on_profession_select)
        scrollbar.config(command=self.profession_listbox.yview)
        
        btn_frame = ttk.Frame(left_frame)
        btn_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(btn_frame, text="Add Profession", command=self.add_profession).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_frame, text="Remove", command=self.remove_profession).pack(side=tk.LEFT, padx=2)
        
        right_frame = ttk.Frame(tab)
        right_frame.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5)
        
        canvas = tk.Canvas(right_frame)
        scrollbar_right = ttk.Scrollbar(right_frame, orient="vertical", command=canvas.yview)
        self.profession_details_frame = ttk.Frame(canvas)
        
        self.profession_details_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=self.profession_details_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar_right.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar_right.pack(side="right", fill="y")
        
        tab.columnconfigure(1, weight=3)
        tab.rowconfigure(0, weight=1)
        
    def create_traits_tab(self):
        
        tab = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(tab, text="Traits")
        
        left_frame = ttk.Frame(tab)
        left_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5)
        
        ttk.Label(left_frame, text="Traits:", font=("Arial", 12, "bold")).pack(anchor=tk.W)
        
        list_frame = ttk.Frame(left_frame)
        list_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        scrollbar = ttk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.trait_listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set, height=20)
        self.trait_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.trait_listbox.bind('<<ListboxSelect>>', self.on_trait_select)
        scrollbar.config(command=self.trait_listbox.yview)
        
        btn_frame = ttk.Frame(left_frame)
        btn_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(btn_frame, text="Add Trait", command=self.add_trait).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_frame, text="Remove", command=self.remove_trait).pack(side=tk.LEFT, padx=2)
        
        right_frame = ttk.Frame(tab)
        right_frame.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5)
        
        canvas = tk.Canvas(right_frame)
        scrollbar_right = ttk.Scrollbar(right_frame, orient="vertical", command=canvas.yview)
        self.trait_details_frame = ttk.Frame(canvas)
        
        self.trait_details_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=self.trait_details_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar_right.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar_right.pack(side="right", fill="y")
        
        tab.columnconfigure(1, weight=3)
        tab.rowconfigure(0, weight=1)
        
    def create_items_tab(self):
        
        tab = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(tab, text="Items")
        
        ttk.Label(tab, text="Custom Items", font=("Arial", 14, "bold")).pack(pady=10)
        ttk.Label(tab, text="Coming in next version!", font=("Arial", 12)).pack(pady=20)
        
    def create_recipes_tab(self):
        
        tab = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(tab, text="Recipes")
        
        ttk.Label(tab, text="Custom Recipes", font=("Arial", 14, "bold")).pack(pady=10)
        ttk.Label(tab, text="Coming in next version!", font=("Arial", 12)).pack(pady=20)
        
    def add_profession(self):
        
        dialog = ProfessionDialog(self.root, self)
        
    def remove_profession(self):
        
        selection = self.profession_listbox.curselection()
        if selection:
            idx = selection[0]
            if messagebox.askyesno("Confirm", "Remove this profession?"):
                del self.mod_data["professions"][idx]
                self.refresh_profession_list()
                self.status_var.set("Profession removed")
                
    def on_profession_select(self, event):
        
        selection = self.profession_listbox.curselection()
        if selection:
            idx = selection[0]
            profession = self.mod_data["professions"][idx]
            self.show_profession_details(profession)
            
    def show_profession_details(self, profession):
        
        for widget in self.profession_details_frame.winfo_children():
            widget.destroy()
            
        ttk.Label(self.profession_details_frame, text="Profession Details", 
                 font=("Arial", 12, "bold")).pack(anchor=tk.W, pady=5)
        
        ttk.Label(self.profession_details_frame, text=f"Name: {profession['name']}", 
                 font=("Arial", 10, "bold")).pack(anchor=tk.W, pady=2)
        
        ttk.Label(self.profession_details_frame, 
                 text=f"Point Cost: {profession['cost']}").pack(anchor=tk.W, pady=2)
        
        ttk.Label(self.profession_details_frame, 
                 text=f"Description: {profession['description']}").pack(anchor=tk.W, pady=2)
        
        if profession.get('skills'):
            ttk.Label(self.profession_details_frame, text="Skills:", 
                     font=("Arial", 10, "bold")).pack(anchor=tk.W, pady=(10, 2))
            for skill, level in profession['skills'].items():
                ttk.Label(self.profession_details_frame, 
                         text=f"  • {skill}: {level}").pack(anchor=tk.W, padx=20)
        
        if profession.get('traits'):
            ttk.Label(self.profession_details_frame, text="Traits:", 
                     font=("Arial", 10, "bold")).pack(anchor=tk.W, pady=(10, 2))
            for trait in profession['traits']:
                ttk.Label(self.profession_details_frame, 
                         text=f"  • {trait}").pack(anchor=tk.W, padx=20)
        
        if profession.get('items'):
            ttk.Label(self.profession_details_frame, text="Starting Items:", 
                     font=("Arial", 10, "bold")).pack(anchor=tk.W, pady=(10, 2))
            for item in profession['items']:
                ttk.Label(self.profession_details_frame, 
                         text=f"  • {item['type']} x{item['count']}").pack(anchor=tk.W, padx=20)
                         
    def refresh_profession_list(self):
        
        self.profession_listbox.delete(0, tk.END)
        for prof in self.mod_data["professions"]:
            self.profession_listbox.insert(tk.END, prof["name"])
            
    def add_trait(self):
        
        dialog = TraitDialog(self.root, self)
        
    def remove_trait(self):
        
        selection = self.trait_listbox.curselection()
        if selection:
            idx = selection[0]
            if messagebox.askyesno("Confirm", "Remove this trait?"):
                del self.mod_data["traits"][idx]
                self.refresh_trait_list()
                self.status_var.set("Trait removed")
                
    def on_trait_select(self, event):
        
        selection = self.trait_listbox.curselection()
        if selection:
            idx = selection[0]
            trait = self.mod_data["traits"][idx]
            self.show_trait_details(trait)
            
    def show_trait_details(self, trait):
        
        for widget in self.trait_details_frame.winfo_children():
            widget.destroy()
            
        ttk.Label(self.trait_details_frame, text="Trait Details", 
                 font=("Arial", 12, "bold")).pack(anchor=tk.W, pady=5)
        
        ttk.Label(self.trait_details_frame, text=f"Name: {trait['name']}", 
                 font=("Arial", 10, "bold")).pack(anchor=tk.W, pady=2)
        
        ttk.Label(self.trait_details_frame, 
                 text=f"Point Cost: {trait['cost']}").pack(anchor=tk.W, pady=2)
        
        ttk.Label(self.trait_details_frame, 
                 text=f"Description: {trait['description']}").pack(anchor=tk.W, pady=2)
                 
    def refresh_trait_list(self):
        
        self.trait_listbox.delete(0, tk.END)
        for trait in self.mod_data["traits"]:
            self.trait_listbox.insert(tk.END, trait["name"])
            
    def new_project(self):
        
        if messagebox.askyesno("New Project", "Create new project? Unsaved changes will be lost."):
            self.mod_data = {
                "mod_name": "",
                "mod_id": "",
                "author": "",
                "description": "",
                "professions": [],
                "traits": [],
                "items": [],
                "recipes": []
            }
            self.mod_name_entry.delete(0, tk.END)
            self.mod_id_entry.delete(0, tk.END)
            self.author_entry.delete(0, tk.END)
            self.description_text.delete('1.0', tk.END)
            self.refresh_profession_list()
            self.refresh_trait_list()
            self.status_var.set("New project created")
            
    def save_project(self):
        
        filename = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        if filename:
            self.mod_data["mod_name"] = self.mod_name_entry.get()
            self.mod_data["mod_id"] = self.mod_id_entry.get()
            self.mod_data["author"] = self.author_entry.get()
            self.mod_data["description"] = self.description_text.get('1.0', tk.END).strip()
            
            with open(filename, 'w') as f:
                json.dump(self.mod_data, f, indent=2)
            
            self.status_var.set(f"Project saved: {filename}")
            messagebox.showinfo("Success", "Project saved successfully!")
            
    def load_project(self):
        
        filename = filedialog.askopenfilename(
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        if filename:
            with open(filename, 'r') as f:
                self.mod_data = json.load(f)
            
            self.mod_name_entry.delete(0, tk.END)
            self.mod_name_entry.insert(0, self.mod_data.get("mod_name", ""))
            
            self.mod_id_entry.delete(0, tk.END)
            self.mod_id_entry.insert(0, self.mod_data.get("mod_id", ""))
            
            self.author_entry.delete(0, tk.END)
            self.author_entry.insert(0, self.mod_data.get("author", ""))
            
            self.description_text.delete('1.0', tk.END)
            self.description_text.insert('1.0', self.mod_data.get("description", ""))
            
            self.refresh_profession_list()
            self.refresh_trait_list()
            
            self.status_var.set(f"Project loaded: {filename}")
            
    def generate_mod(self):
        
        if not self.mod_name_entry.get() or not self.mod_id_entry.get():
            messagebox.showerror("Error", "Please fill in Mod Name and Mod ID")
            return
            
        if not self.mod_data["professions"] and not self.mod_data["traits"]:
            messagebox.showerror("Error", "Please add at least one profession or trait")
            return
        
        output_dir = filedialog.askdirectory(title="Select Output Directory")
        if not output_dir:
            return
            
        try:
            generator = ModGenerator(self.mod_data, self)
            generator.generate(output_dir)
            
            messagebox.showinfo("Success", 
                f"Mod generated successfully!\n\nLocation: {output_dir}/{self.mod_data['mod_id']}")
            self.status_var.set("Mod generated successfully!")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate mod: {str(e)}")
            self.status_var.set("Error generating mod")
            
    def show_about(self):
        
        about_text = 
        
        messagebox.showinfo("About PropModCreator", about_text)
        
    def show_docs(self):
        
        docs_text = 
        
        messagebox.showinfo("Documentation", docs_text)

class ProfessionDialog:
    
    def __init__(self, parent, app):
        self.app = app
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Add Profession")
        self.dialog.geometry("600x700")
        self.dialog.grab_set()
        
        self.skills_data = {}
        self.traits_list = []
        self.items_list = []
        
        self.create_ui()
        
    def create_ui(self):
        
        main_frame = ttk.Frame(self.dialog, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(main_frame, text="Profession Name:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.name_entry = ttk.Entry(main_frame, width=40)
        self.name_entry.grid(row=0, column=1, pady=5, padx=5)
        
        ttk.Label(main_frame, text="Point Cost:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.cost_spinbox = ttk.Spinbox(main_frame, from_=-10, to=10, width=10)
        self.cost_spinbox.set(0)
        self.cost_spinbox.grid(row=1, column=1, sticky=tk.W, pady=5, padx=5)
        
        ttk.Label(main_frame, text="Description:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.description_text = tk.Text(main_frame, height=3, width=40)
        self.description_text.grid(row=2, column=1, pady=5, padx=5)
        
        ttk.Label(main_frame, text="Skills:", font=("Arial", 10, "bold")).grid(
            row=3, column=0, columnspan=2, sticky=tk.W, pady=(10, 5))
        
        skills_frame = ttk.LabelFrame(main_frame, text="Add Skill", padding="5")
        skills_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Label(skills_frame, text="Skill:").grid(row=0, column=0, padx=5)
        self.skill_combo = ttk.Combobox(skills_frame, values=[
            "Carpentry", "Woodwork", "Farming", "Fishing", "Trapping", "Foraging",
            "Mechanics", "Electricity", "Metalworking", "Tailoring",
            "Cooking", "FirstAid",
            "Fitness", "Strength", "Sprinting", "Lightfooted", "Nimble", "Sneak",
            "Aiming", "Reloading", "Axe", "Blunt", "SmallBlunt", "LongBlade", 
            "SmallBlade", "Spear", "Maintenance"
        ], width=15)
        self.skill_combo.grid(row=0, column=1, padx=5)
        
        ttk.Label(skills_frame, text="Level:").grid(row=0, column=2, padx=5)
        self.skill_level_spinbox = ttk.Spinbox(skills_frame, from_=1, to=10, width=5)
        self.skill_level_spinbox.set(1)
        self.skill_level_spinbox.grid(row=0, column=3, padx=5)
        
        ttk.Button(skills_frame, text="Add Skill", command=self.add_skill).grid(
            row=0, column=4, padx=5)
        
        self.skills_listbox = tk.Listbox(main_frame, height=5)
        self.skills_listbox.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5, padx=5)
        
        ttk.Button(main_frame, text="Remove Skill", command=self.remove_skill).grid(
            row=6, column=0, columnspan=2, pady=5)
        
        ttk.Label(main_frame, text="Traits:", font=("Arial", 10, "bold")).grid(
            row=7, column=0, columnspan=2, sticky=tk.W, pady=(10, 5))
        
        traits_frame = ttk.LabelFrame(main_frame, text="Add Trait", padding="5")
        traits_frame.grid(row=8, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Label(traits_frame, text="Trait:").grid(row=0, column=0, padx=5)
        
        vanilla_traits = [
            "Handy", "Outdoorsman", "FastLearner", "Organized", "Keen Hearing",
            "Eagle Eyed", "Graceful", "Lucky", "Dextrous", "Athletic",
            "Strong", "Stout", "Brave", "Resilient", "FastHealer",
            "LightEater", "Inconspicuous"
        ]
        
        custom_traits = [trait["name"] for trait in self.app.mod_data["traits"]]
        all_traits = vanilla_traits + custom_traits
        
        self.trait_combo = ttk.Combobox(traits_frame, values=all_traits, width=20)
        self.trait_combo.grid(row=0, column=1, padx=5)
        
        ttk.Button(traits_frame, text="Add Trait", command=self.add_trait).grid(
            row=0, column=2, padx=5)
        
        self.traits_listbox = tk.Listbox(main_frame, height=4)
        self.traits_listbox.grid(row=9, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5, padx=5)
        
        ttk.Button(main_frame, text="Remove Trait", command=self.remove_trait).grid(
            row=10, column=0, columnspan=2, pady=5)
        
        ttk.Label(main_frame, text="Starting Items:", font=("Arial", 10, "bold")).grid(
            row=11, column=0, columnspan=2, sticky=tk.W, pady=(10, 5))
        
        items_frame = ttk.LabelFrame(main_frame, text="Add Item", padding="5")
        items_frame.grid(row=12, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Label(items_frame, text="Item Type:").grid(row=0, column=0, padx=5)
        self.item_entry = ttk.Entry(items_frame, width=20)
        self.item_entry.insert(0, "Base.")
        self.item_entry.grid(row=0, column=1, padx=5)
        
        ttk.Label(items_frame, text="Count:").grid(row=0, column=2, padx=5)
        self.item_count_spinbox = ttk.Spinbox(items_frame, from_=1, to=100, width=5)
        self.item_count_spinbox.set(1)
        self.item_count_spinbox.grid(row=0, column=3, padx=5)
        
        ttk.Button(items_frame, text="Add Item", command=self.add_item).grid(
            row=0, column=4, padx=5)
        
        self.items_listbox = tk.Listbox(main_frame, height=4)
        self.items_listbox.grid(row=13, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5, padx=5)
        
        ttk.Button(main_frame, text="Remove Item", command=self.remove_item).grid(
            row=14, column=0, columnspan=2, pady=5)
        
        btn_frame = ttk.Frame(main_frame)
        btn_frame.grid(row=15, column=0, columnspan=2, pady=20)
        
        ttk.Button(btn_frame, text="Save Profession", command=self.save).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Cancel", command=self.dialog.destroy).pack(side=tk.LEFT, padx=5)
        
        main_frame.columnconfigure(1, weight=1)
        
    def add_skill(self):
        
        skill = self.skill_combo.get()
        level = self.skill_level_spinbox.get()
        
        if skill:
            self.skills_data[skill] = int(level)
            self.skills_listbox.insert(tk.END, f"{skill}: {level}")
            
    def remove_skill(self):
        
        selection = self.skills_listbox.curselection()
        if selection:
            idx = selection[0]
            text = self.skills_listbox.get(idx)
            skill = text.split(":")[0]
            del self.skills_data[skill]
            self.skills_listbox.delete(idx)
            
    def add_trait(self):
        
        trait = self.trait_combo.get()
        if trait and trait not in self.traits_list:
            self.traits_list.append(trait)
            self.traits_listbox.insert(tk.END, trait)
            
    def remove_trait(self):
        
        selection = self.traits_listbox.curselection()
        if selection:
            idx = selection[0]
            trait = self.traits_listbox.get(idx)
            self.traits_list.remove(trait)
            self.traits_listbox.delete(idx)
            
    def add_item(self):
        
        item_type = self.item_entry.get()
        count = int(self.item_count_spinbox.get())
        
        if item_type:
            self.items_list.append({"type": item_type, "count": count})
            self.items_listbox.insert(tk.END, f"{item_type} x{count}")
            
    def remove_item(self):
        
        selection = self.items_listbox.curselection()
        if selection:
            idx = selection[0]
            del self.items_list[idx]
            self.items_listbox.delete(idx)
            
    def save(self):
        
        name = self.name_entry.get()
        
        if not name:
            messagebox.showerror("Error", "Please enter a profession name")
            return
            
        profession = {
            "name": name,
            "cost": int(self.cost_spinbox.get()),
            "description": self.description_text.get('1.0', tk.END).strip(),
            "skills": self.skills_data,
            "traits": self.traits_list,
            "items": self.items_list
        }
        
        self.app.mod_data["professions"].append(profession)
        self.app.refresh_profession_list()
        self.app.status_var.set(f"Added profession: {name}")
        
        self.dialog.destroy()

class TraitDialog:
    
    def __init__(self, parent, app):
        self.app = app
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Add Trait")
        self.dialog.geometry("500x300")
        self.dialog.grab_set()
        
        self.create_ui()
        
    def create_ui(self):
        
        main_frame = ttk.Frame(self.dialog, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(main_frame, text="Trait Name:").grid(row=0, column=0, sticky=tk.W, pady=10)
        self.name_entry = ttk.Entry(main_frame, width=40)
        self.name_entry.grid(row=0, column=1, pady=10, padx=5)
        
        ttk.Label(main_frame, text="Point Cost:").grid(row=1, column=0, sticky=tk.W, pady=10)
        cost_frame = ttk.Frame(main_frame)
        cost_frame.grid(row=1, column=1, sticky=tk.W, pady=10, padx=5)
        
        self.cost_spinbox = ttk.Spinbox(cost_frame, from_=-10, to=10, width=10)
        self.cost_spinbox.set(0)
        self.cost_spinbox.pack(side=tk.LEFT)
        
        ttk.Label(cost_frame, text="(Negative = costs points, Positive = gives points)", 
                 font=("Arial", 8)).pack(side=tk.LEFT, padx=10)
        
        ttk.Label(main_frame, text="Description:").grid(row=2, column=0, sticky=tk.W, pady=10)
        self.description_text = tk.Text(main_frame, height=5, width=40)
        self.description_text.grid(row=2, column=1, pady=10, padx=5)
        
        btn_frame = ttk.Frame(main_frame)
        btn_frame.grid(row=3, column=0, columnspan=2, pady=20)
        
        ttk.Button(btn_frame, text="Save Trait", command=self.save).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Cancel", command=self.dialog.destroy).pack(side=tk.LEFT, padx=5)
        
        main_frame.columnconfigure(1, weight=1)
        
    def save(self):
        
        name = self.name_entry.get()
        
        if not name:
            messagebox.showerror("Error", "Please enter a trait name")
            return
            
        trait = {
            "name": name,
            "cost": int(self.cost_spinbox.get()),
            "description": self.description_text.get('1.0', tk.END).strip()
        }
        
        self.app.mod_data["traits"].append(trait)
        self.app.refresh_trait_list()
        self.app.status_var.set(f"Added trait: {name}")
        
        self.dialog.destroy()

class ModGenerator:
    
    def __init__(self, mod_data, app):
        self.mod_data = mod_data
        self.app = app
        
        self.mod_data["mod_name"] = app.mod_name_entry.get()
        self.mod_data["mod_id"] = app.mod_id_entry.get()
        self.mod_data["author"] = app.author_entry.get()
        self.mod_data["description"] = app.description_text.get('1.0', tk.END).strip()
        self.mod_data["version"] = app.version_entry.get()
        
    def generate(self, output_dir):
        
        mod_path = Path(output_dir) / self.mod_data["mod_id"]
        mod_path.mkdir(exist_ok=True)
        
        lua_shared = mod_path / "media" / "lua" / "shared"
        lua_shared.mkdir(parents=True, exist_ok=True)
        
        self.generate_mod_info(mod_path)
        self.generate_lua_file(lua_shared)
        self.generate_readme(mod_path)
        
    def generate_mod_info(self, mod_path):
        
        content = f
        with open(mod_path / "mod.info", 'w') as f:
            f.write(content)
            
    def generate_lua_file(self, lua_path):
        
        mod_id = self.mod_data['mod_id']
        
        content = f
        
        if self.mod_data["professions"]:
            content += f
            
            for prof in self.mod_data["professions"]:
                content += f
                for skill, level in prof.get('skills', {}).items():
                    content += f"            {skill} = {level},\n"
                    
                content += "        },\n"
                content += "        traits = {"
                
                for trait in prof.get('traits', []):
                    content += f'"{trait}", '
                    
                content += "},\n"
                content += "    })\n"
                
                for item in prof.get('items', []):
                    content += f
                    
            content += "end\n\n"
        else:
            content += f
        
        if self.mod_data["traits"]:
            content += f
            
            for trait in self.mod_data["traits"]:
                content += f
                
            content += "end\n\n"
        else:
            content += f
        
        content += f
        
        with open(lua_path / f"{mod_id}.lua", 'w') as f:
            f.write(content)
            
    def generate_readme(self, mod_path):
        
        content = f
        
        if self.mod_data["professions"]:
            content += "### Professions\n\n"
            for prof in self.mod_data["professions"]:
                content += f"#### {prof['name']}\n"
                content += f"**Cost:** {prof['cost']} points\n\n"
                content += f"{prof['description']}\n\n"
                
                if prof.get('skills'):
                    content += "**Skills:**\n"
                    for skill, level in prof['skills'].items():
                        content += f"- {skill}: {level}\n"
                    content += "\n"
                    
                if prof.get('traits'):
                    content += "**Traits:**\n"
                    for trait in prof['traits']:
                        content += f"- {trait}\n"
                    content += "\n"
                    
                if prof.get('items'):
                    content += "**Starting Items:**\n"
                    for item in prof['items']:
                        content += f"- {item['type']} x{item['count']}\n"
                    content += "\n"
                    
        if self.mod_data["traits"]:
            content += "### Traits\n\n"
            for trait in self.mod_data["traits"]:
                content += f"#### {trait['name']}\n"
                content += f"**Cost:** {trait['cost']} points\n\n"
                content += f"{trait['description']}\n\n"
                
        content += 
        
        with open(mod_path / "README.md", 'w') as f:
            f.write(content)

def main():
    root = tk.Tk()
    app = PropModCreator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
