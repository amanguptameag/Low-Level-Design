from cowin_app import CowinApp

app = CowinApp()

# Register users
user1_id = app.register_user("Alice")
user2_id = app.register_user("Bob")

# Add centers
center1_id = app.add_center("Center A", "Location 1")
center2_id = app.add_center("Center B", "Location 2")


# Add slots to centers
app.add_slot_to_center(center1_id, "10:00 AM")
app.add_slot_to_center(center1_id, "11:00 AM")
app.add_slot_to_center(center2_id, "10:00 AM")
app.add_slot_to_center(center2_id, "11:00 AM")

# Book slots
app.book_slot(user1_id, center1_id, "10:00 AM")
app.book_slot(user2_id, center2_id, "11:00 AM")
app.book_slot(user2_id, center1_id, "10:00 AM")  # Attempt to book an already booked slot

# View all centers
app.view_centers()

# View all users
app.view_users()



