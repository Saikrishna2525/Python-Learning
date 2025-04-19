# 5)Movie Ticket Pricing System
# You are working on a movie ticket pricing system for a theater, where the ticket price varies based on the following factors:
# Movie Type: The movie can either be in 3D or 2D.

# Age of the Viewer: The ticket price changes depending on the viewer's age:
# For viewers younger than 18, there is a lower price.
# For viewers between the ages of 18 and 60, the price is a bit higher.
# For viewers older than 60, the price is slightly discounted.
# Additionally, there is a membership status that can affect the ticket price:
# Members receive a 20% discount on the ticket price.

# Pricing Logic:
# For 3D Movies:

# If the viewer's age is less than 18 → ₹100
# If the viewer's age is between 18 and 60 → ₹150
# If the viewer’s age is above 60 → ₹120

# For 2D Movies:

# If the viewer's age is less than 18 → ₹80
# If the viewer's age is between 18 and 60 → ₹100
# If the viewer’s age is above 60 → ₹90
# Your task is to calculate the final ticket price based on the following inputs:
# Movie Type (3D or 2D)

# Age of the viewer


# Membership Status (either "member" or "non-member")

system_data = {
    "2d":{
        "Child":80,
        "Adult":100,
        "Senior Citizen":"90 (Discounted Price)"
    },
    "3d":{
        "Child":100,
        "Adult":150,
        "Senior Citizen":"120 (Discounted Price)"
    }
}

Membership_Discount = 0.2 
