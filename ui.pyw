import tkinter as tk
import tkinter.ttk as ttk
import bedrock_tools as mc


def backup_settings():
    window.destroy()
    mc.open_backup_settings_gui()
    open_window()

def open_window():
    global window
    def tab_changed(event):
        selected_tab = tab_control.tab(tab_control.select(), "text")
        if selected_tab == "Info":
            print("Info tab clicked")
            # Run mc.get_world_dict() and display the output in the Worlds tab
            world_dict = mc.get_world_dict()
            world_dict_text.config(state="normal")
            world_dict_text.delete("1.0", tk.END)
            for item in world_dict:
                world_dict_text.insert(tk.END, str(item) + "\n")
            world_dict_text.config(state="disabled")

            # Run mc.get_resource_pack_info() and display the output in the Resource Packs tab
            resource_pack_info = mc.get_resource_pack_info()
            resource_pack_text.config(state="normal")
            resource_pack_text.delete("1.0", tk.END)
            for item in resource_pack_info:
                resource_pack_text.insert(tk.END, str(item) + "\n")
            resource_pack_text.config(state="disabled")
        elif selected_tab == "Backup":
            backup_path = backup_path_entry.get()
            backup_worlds_button.config(command=lambda: mc.backup_worlds(backup_path))
            backup_everything_button.config(command=lambda: mc.backup_main(backup_path))



    # Create the main window
    window = tk.Tk()
    window.title("Bedrock Launcher")
    window.state('zoomed')

    # Set the pixel font and larger font size
    font_style = ("Pixel", 24)

    # Create the tabbed layout
    tab_control = ttk.Notebook(window, style="Custom.TNotebook")

    # Define the custom style for the tabs
    style = ttk.Style()
    style.configure("Custom.TNotebook.Tab", font=font_style, padding=[20, 10], width=20)

    # Configure the tab control to use the custom style
    tab_control.configure(style="Custom.TNotebook")

    # Create the Play tab
    play_tab = ttk.Frame(tab_control)
    tab_control.add(play_tab, text="Play")
    tab_control.pack(expand=1, fill="both")

    # Add title to Play tab
    play_title = tk.Label(play_tab, text="Minecraft Bedrock Launcher", font=font_style)
    play_title.pack(pady=40)

    # Create the Play buttons with larger dimensions and updated colors
    play_button = tk.Button(play_tab, text="Play", font=font_style, fg="white", bg="#2ecc71", width=30, height=4, command=mc.start_game)
    play_button.pack(pady=10)

    fov_button = tk.Button(play_tab, text="Play with FOV Changer", font=font_style, fg="white", bg="#1abc9c", width=30, height=4, command=lambda: mc.start_game(True))
    fov_button.pack(pady=10)

    fov_changer_button = tk.Button(play_tab, text="FOV Changer", font=font_style, fg="white", bg="blue", width=30, height=4, command=mc.fov_changer)
    fov_changer_button.pack(pady=10)

    # Create the Info tab
    info_tab = ttk.Frame(tab_control)
    tab_control.add(info_tab, text="Info")

    # Add title to Info tab
    info_title = tk.Label(info_tab, text="Minecraft Bedrock Info", font=font_style)
    info_title.pack(pady=40)

    # ...

    world_dict_text = tk.Text(info_tab, width=60, height=10, state="disabled")
    world_dict_text.pack(padx=10, pady=10)

    # Create a label for the resource packs info box title
    resource_packs_label = tk.Label(info_tab, text="Resource Packs", font=font_style)
    resource_packs_label.pack()

    # Create a text widget to display the resource pack info
    resource_pack_text = tk.Text(info_tab, width=60, height=10, state="disabled")
    resource_pack_text.pack(padx=10, pady=10)

    # Bind the tab_changed function to the tab changed event
    tab_control.bind("<<NotebookTabChanged>>", tab_changed)


    # Create a label for the behavior packs info box title
    behavior_packs_label = tk.Label(info_tab, text="Behavior Packs", font=font_style)
    behavior_packs_label.pack()

    # Create a text widget to display the behavior pack info
    behavior_pack_text = tk.Text(info_tab, width=60, height=10, state="disabled")
    behavior_pack_text.pack(padx=10, pady=10)

    def tab_changed(event):
        selected_tab = tab_control.tab(tab_control.select(), "text")
        if selected_tab == "Info":
            # Run mc.get_world_dict() and display the output in the Worlds tab
            world_dict = mc.get_world_dict()
            world_dict_text.config(state="normal")
            world_dict_text.delete("1.0", tk.END)
            for item in world_dict:
                world_dict_text.insert(tk.END, str(item) + "\n")
            world_dict_text.config(state="disabled")

            # Run mc.get_resource_pack_info() and display the output in the Resource Packs tab
            resource_pack_info = mc.get_resource_pack_info()
            resource_pack_text.config(state="normal")
            resource_pack_text.delete("1.0", tk.END)
            for item in resource_pack_info:
                resource_pack_text.insert(tk.END, str(item) + "\n")
            resource_pack_text.config(state="disabled")

            # Run mc.get_behavior_pack_info() and display the output in the Behavior Packs tab
            behavior_pack_info = mc.get_behavior_pack_info()
            behavior_pack_text.config(state="normal")
            behavior_pack_text.delete("1.0", tk.END)
            for item in behavior_pack_info:
                behavior_pack_text.insert(tk.END, str(item) + "\n")
            behavior_pack_text.config(state="disabled")

    # Bind the tab_changed function to the tab changed event
    tab_control.bind("<<NotebookTabChanged>>", tab_changed)











    # Create the Run tab
    run_tab = ttk.Frame(tab_control)
    tab_control.add(run_tab, text="Run")

    # Add title to Run tab
    run_title = tk.Label(run_tab, text="Run Commands", font=font_style)
    run_title.pack(pady=40)

    # Create buttons for additional functionalities

    def import_pack():
        import tkinter as tk

        def import_pack():
            # Get the value from the text box
            pack_path = text_box.get()
            
            # Call the mc.import_pack() function with the pack path
            mc.import_pack(pack_path)

            #close the window
            window.destroy()

        # Create the Tkinter window
        window = tk.Tk()
        window.title("import pack (path)")
        window.geometry('400x300')
        # Create the text input box
        text_box = tk.Entry(window)
        text_box.pack()

        # Create the button
        import_button = tk.Button(window, text="Import", command=import_pack)
        import_button.pack()

        # Start the Tkinter event loop
        window.mainloop()





    import_pack_button = tk.Button(run_tab, text="Import Pack", font=font_style, command=import_pack)

    def apply_resource_packs():
        import tkinter as tk

        def apply_resource_pack():
            world_folder = world_folder_entry.get()
            resource_pack_uuid = resource_pack_uuid_entry.get()
            mc.apply_resource_pack(world_folder, resource_pack_uuid)
            window.destroy()  # Close the window after executing mc.apply_resource_pack

        # Create the main window
        window = tk.Tk()
        window.geometry('400x300')
        # Set the window title
        window.title("Resource Pack Applier")

        # Create the world folder label and entry
        world_folder_label = tk.Label(window, text="World Folder:")
        world_folder_label.pack()
        world_folder_entry = tk.Entry(window)
        world_folder_entry.pack()

        # Create the resource pack UUID label and entry
        resource_pack_uuid_label = tk.Label(window, text="Resource Pack UUID:")
        resource_pack_uuid_label.pack()
        resource_pack_uuid_entry = tk.Entry(window)
        resource_pack_uuid_entry.pack()

        # Create the apply button
        apply_button = tk.Button(window, text="Apply", command=apply_resource_pack)
        apply_button.pack()

        # Start the Tkinter event loop
        window.mainloop()

    apply_resource_packs_button = tk.Button(run_tab, text="Apply Resource Packs", font=font_style, command=apply_resource_packs)

    def apply_behavior_pack():
        import tkinter as tk

        def apply_behavior_pack():
            world_folder = world_folder_entry.get()
            behavior_pack_uuid = behavior_pack_uuid_entry.get()
            mc.apply_behavior_pack(world_folder, behavior_pack_uuid)
            window.destroy()  # Close the window after executing mc.apply_resource_pack

        # Create the main window
        window = tk.Tk()
        window.geometry('400x300')
        # Set the window title
        window.title("Behavior Pack Applier")

        # Create the world folder label and entry
        world_folder_label = tk.Label(window, text="World Folder:")
        world_folder_label.pack()
        world_folder_entry = tk.Entry(window)
        world_folder_entry.pack()

        # Create the behavior pack UUID label and entry
        behavior_pack_uuid_label = tk.Label(window, text="Behavior Pack UUID:")
        behavior_pack_uuid_label.pack()
        behavior_pack_uuid_entry = tk.Entry(window)
        behavior_pack_uuid_entry.pack()

        # Create the apply button
        apply_button = tk.Button(window, text="Apply", command=apply_behavior_pack)
        apply_button.pack()

        # Start the Tkinter event loop
        window.mainloop()

    apply_behavior_pack_button = tk.Button(run_tab, text="Apply Behavior Pack", font=font_style, command=apply_behavior_pack)

    def delete_resource_pack():
        import tkinter as tk

        def delete_resource_pack():
            # Get the value from the text box
            pack_path = text_box.get()
            
            # Call the mc.import_pack() function with the pack path
            mc.delete_resource_pack(pack_path)

            #close the window
            window.destroy()

        # Create the Tkinter window
        window = tk.Tk()
        window.geometry('400x300')
        window.title("Delete recource pack (uuid)")

        # Create the text input box
        text_box = tk.Entry(window)
        text_box.pack()

        # Create the button
        import_button = tk.Button(window, text="delete", command=delete_resource_pack)
        import_button.pack()

        # Start the Tkinter event loop
        window.mainloop()



    delete_resource_pack_button = tk.Button(run_tab, text="Delete Resource Pack", font=font_style, command=delete_resource_pack)

    def delete_behavior_pack():
        import tkinter as tk

        def delete_behavior_pack():
            # Get the value from the text box
            pack_path = text_box.get()
            
            # Call the mc.import_pack() function with the pack path
            mc.delete_behavior_pack(pack_path)

            #close the window
            window.destroy()

        # Create the Tkinter window
        window = tk.Tk()
        window.title("Delete behavior pack (uuid)")
        window.geometry('400x300')
        # Create the text input box
        text_box = tk.Entry(window)
        text_box.pack()

        # Create the button
        import_button = tk.Button(window, text="delete", command=delete_behavior_pack)
        import_button.pack()

        # Start the Tkinter event loop
        window.mainloop()

    delete_behavior_pack_button = tk.Button(run_tab, text="Delete Behavior Pack", font=font_style, command=delete_behavior_pack)

    def clear_pack_history():
        def clear_histoy():
            # Get the value from the text box
            pack_path = text_box.get()
            
            # Call the mc.import_pack() function with the pack path
            mc.clear_pack_history(pack_path)

            #close the window
            window.destroy()

        # Create the Tkinter window
        window = tk.Tk()
        window.title("clear world pack history (folder name)")
        window.geometry('400x300')
        # Create the text input box
        text_box = tk.Entry(window)
        text_box.pack()

        # Create the button
        import_button = tk.Button(window, text="Import", command=clear_histoy)
        import_button.pack()

        # Start the Tkinter event loop
        window.mainloop()

    clear_pack_history_button = tk.Button(run_tab, text="Clear Pack History", font=font_style, command=clear_pack_history)

    def disable_resource_packs():
        def disable_packs():
            # Get the value from the text box
            pack_path = text_box.get()
            
            # Call the mc.import_pack() function with the pack path
            mc.disable_resource_packs(pack_path)

            #close the window
            window.destroy()

        # Create the Tkinter window
        window = tk.Tk()
        window.title("clear world resource packs (folder name)")
        window.geometry('400x300')
        # Create the text input box
        text_box = tk.Entry(window)
        text_box.pack()

        # Create the button
        import_button = tk.Button(window, text="Import", command=disable_packs)
        import_button.pack()

        # Start the Tkinter event loop
        window.mainloop()

    disable_resource_packs_button = tk.Button(run_tab, text="Disable Resource Packs", font=font_style, command=disable_resource_packs)

    def disable_behavior_packs():
        def disable_packs():
            # Get the value from the text box
            pack_path = text_box.get()
            
            # Call the mc.import_pack() function with the pack path
            mc.disable_behavior_packs(pack_path)

            #close the window
            window.destroy()

        # Create the Tkinter window
        window = tk.Tk()
        window.title("clear world behavior packs (folder name)")
        window.geometry('400x300')
        # Create the text input box
        text_box = tk.Entry(window)
        text_box.pack()

        # Create the button
        import_button = tk.Button(window, text="Import", command=disable_packs)
        import_button.pack()

        # Start the Tkinter event loop
        window.mainloop()

    disable_behavior_packs_button = tk.Button(run_tab, text="Disable Behavior Packs", font=font_style, command=disable_behavior_packs)

    # Pack the buttons vertically
    import_pack_button.pack(pady=5)
    apply_resource_packs_button.pack(pady=5)
    apply_behavior_pack_button.pack(pady=5)
    delete_resource_pack_button.pack(pady=5)
    delete_behavior_pack_button.pack(pady=5)
    clear_pack_history_button.pack(pady=5)
    disable_resource_packs_button.pack(pady=5)
    disable_behavior_packs_button.pack(pady=5)




    # def tab_changed(event):
    #     selected_tab = tab_control.tab(tab_control.select(), "text")
    #     if selected_tab == "Info":
    #         # Run the existing code for the Info tab
    #         ...
    #     elif selected_tab == "Backup":
    #         backup_path = backup_path_entry.get()
    #         backup_worlds_button.config(command=lambda: mc.backup_worlds(backup_path))
    #         backup_everything_button.config(command=lambda: mc.backup_main(backup_path))

    # Create the Backup tab
    backup_tab = ttk.Frame(tab_control)
    tab_control.add(backup_tab, text="Backup")

    # Add components to the Backup tab
    backup_path_label = tk.Label(backup_tab, text="Backup Path:", font=("Arial", 18))
    backup_path_label.pack()

    backup_path_entry = tk.Entry(backup_tab, font=("Arial", 15), width=50)
    backup_path_entry.pack()

    backup_worlds_button = tk.Button(backup_tab, text="Backup Worlds", font=("Arial", 15), command=lambda: mc.backup_worlds(backup_path_entry.get()))
    backup_worlds_button.pack(pady=10)

    backup_everything_button = tk.Button(backup_tab, text="Backup Everything", font=("Arial", 15), command=lambda: mc.backup_main(backup_path_entry.get()))
    backup_everything_button.pack(pady=10)

    backup_settings_button = tk.Button(backup_tab, text="Auto Backup", font=("Arial", 15), command=lambda: backup_settings())
    backup_settings_button.pack(pady=10)

    # Update the tab_changed function
    tab_control.bind("<<NotebookTabChanged>>", tab_changed)





    # Run the main window loop
    window.mainloop()

if __name__ == "__main__":
    open_window()