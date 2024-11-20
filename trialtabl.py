import customtkinter as ctk

# Initialize the app
app = ctk.CTk()
app.geometry("500x400")
app.title("CustomTkinter Tabs Example")

# Set the background of the window to white
app.configure(bg="white")

# Configure appearance
ctk.set_appearance_mode("light")  # Dark theme for the window
ctk.set_default_color_theme("blue")

# Create a TabView
tab_view = ctk.CTkTabview(app, width=500, height=400, fg_color="transparent")
tab_view.pack(pady=0, padx=0, fill="both", expand=True)
tab_view._segmented_button.grid_configure(sticky="w")

# Add tabs
tab1 = tab_view.add("Tab 1")
tab2 = tab_view.add("Tab 2")
tab3 = tab_view.add("Tab 3")

# Create a rounded frame for Tab 1 (the form container)
frame = ctk.CTkFrame(tab1, corner_radius=20, fg_color="white", width=400, height=300, border_color="black", border_width=2)
frame.pack(pady=50, padx=50)

# Add a title at the top of the form (allow it to go outside the frame)
form_title = ctk.CTkLabel(frame, text="Form", font=("Arial", 16, "bold"), text_color="black")

# Position the title outside the border
form_title.place(x=20, y=-12)  # Negative y-value to make the title go outside the border

# Add labels and entry fields inside the frame
for i in range(3):
    label = ctk.CTkLabel(frame, text="Label one:", font=("Arial", 14), text_color="black")
    label.place(x=20, y=50 + i * 60)  # Adjust y-coordinate for each label
    
    entry = ctk.CTkEntry(frame, width=200, height=30, border_width=1)
    entry.place(x=120, y=50 + i * 60)  # Adjust y-coordinate for each entry

# Run the app
app.mainloop()
