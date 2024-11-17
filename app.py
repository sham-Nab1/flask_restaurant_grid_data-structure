from flask import Flask, render_template

app = Flask(__name__)


# TODO: Restaurant List of Dictionaries
# image_url, restaurant_name, status, location, id
restaurants = [
    {
        "id": 1,
        "location": "Makati",
        "restaurant_name": "Restaurant One",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/67468/pexels-photo-67468.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },
    {
        "id": 2,
        "location": "Pasig",
        "restaurant_name": "Restaurant Two",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/25858122/pexels-photo-25858122/free-photo-of-patio-of-cafe.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },{
        "id": 3,
        "location": "Mandaluyong",
        "restaurant_name": "Restaurant Three",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/16550341/pexels-photo-16550341/free-photo-of-facade-of-urban-building.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },{
        "id": 4,
        "location": "Quezon CIty",
        "restaurant_name": "Restaurant Four",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/12935080/pexels-photo-12935080.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },{
        "id": 5,
        "location": "Alabang",
        "restaurant_name": "Restaurant Five",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/8921562/pexels-photo-8921562.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },{
        "id": 6,
        "location": "Pasig",
        "restaurant_name": "Restaurant Six",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/14646764/pexels-photo-14646764.jpeg?auto=compress&cs=tinysrgb&w=600&lazy=load"
    },{
        "id": 7,
        "location": "Paranaque City, Metro Manila",
        "restaurant_name": "Teds Oldtimer La Paz Batchoy",
        "status": "Closed",
        "image_url": "https://secret-ph.com/wp-content/uploads/2023/01/Teds-Oldtimer-La-Paz-Batchoy.jpg.webp"
    },{
        "id": 8,
        "location": "Bacolod",
        "restaurant_name": "Manokan Country",
        "status": "Closed",
        "image_url": "https://secret-ph.com/wp-content/uploads/2023/01/Manokan-Country.jpg.webp"
    },{
        "id": 9,
        "location": "In Between SM Lanang and Dcwd",
        "restaurant_name": "Blue Post Boiling Crabs and Shrimps",
        "status": "Open",
        "image_url": "https://secret-ph.com/wp-content/uploads/2023/01/Blue-Post-Boiling-Crabs-and-Shrimps.jpg.webp"
    },{
        "id": 10,
        "location": "Davao del Sur",
        "restaurant_name": "Balik Bukid Farm and Kitchen",
        "status": "Closed",
        "image_url": "https://secret-ph.com/wp-content/uploads/2023/01/Balik-Bukid-Farm-and-Kitchen.jpg.webp"
    },{
        "id": 11,
        "location": "Taguig City",
        "restaurant_name": "Bench Cafe",
        "status": "Open",
        "image_url": "https://secret-ph.com/wp-content/uploads/2023/01/Bench-Cafe.jpg.webp"
    },{
        "id": 12,
        "location": "Paranaque",
        "restaurant_name": "Bamba Bistro",
        "status": "Open",
        "image_url": "https://secret-ph.com/wp-content/uploads/2023/01/Bamba-Bistro.jpg.webp"
    },{
        "id": 13,
        "location": "Makati",
        "restaurant_name": "Beso Beso",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/OIP.2gwhcqG-5xteRH11t0DeXgHaFi?rs=1&pid=ImgDetMain"
    },{
        "id": 14,
        "location": "Tagaytay",
        "restaurant_name": "Breakfast at Antonios",
        "status": "Closed",
        "image_url": "https://secret-ph.com/wp-content/uploads/2023/01/Breakfast-at-Antonios.jpg.webp"
    },{
        "id": 15,
        "location": "Makati City",
        "restaurant_name": "Farmers Table Tagaytay",
        "status": "Open",
        "image_url": "https://secret-ph.com/wp-content/uploads/2023/01/Farmers-Table-Tagaytay.jpg.webp"
    },{
        "id": 16,
        "location": "Cebu City",
        "restaurant_name": "Cafe Laguna",
        "status": "Closed",
        "image_url": "https://secret-ph.com/wp-content/uploads/2023/01/Cafe-Laguna.jpg.webp"
    },{
        "id": 17,
        "location": "Makati",
        "restaurant_name": "Milky Way Cafe",
        "status": "Open",
        "image_url": "https://secret-ph.com/wp-content/uploads/2023/01/Milky-Way-Cafe.jpg.webp"
    },{
        "id": 18,
        "location": " Makati",
        "restaurant_name": "Grace Park Dining",
        "status": "Open",
        "image_url": "https://secret-ph.com/wp-content/uploads/2023/01/grace.jpg.webp"
    },{
        "id": 19,
        "location": "Quezon City",
        "restaurant_name": "Hapag",
        "status": "Closed",
        "image_url": "https://secret-ph.com/wp-content/uploads/2023/01/Hapag.jpg.webp"
    },{
        "id": 20,
        "location": "Makati",
        "restaurant_name": "Lampara",
        "status": "Closed",
        "image_url": "https://secret-ph.com/wp-content/uploads/2023/01/Lampara.jpg.webp"
    },{
        "id": 21,
        "location": "Mandaluyong City",
        "restaurant_name": "Mesa",
        "status": "Open",
        "image_url": "https://secret-ph.com/wp-content/uploads/2023/01/Mesa.jpg.webp"
    },{
        "id": 22,
        "location": "Makati, Metro Manila",
        "restaurant_name": "Metiz",
        "status": "Closed",
        "image_url": "https://secret-ph.com/wp-content/uploads/2023/01/Metiz.jpg.webp"
    },{
        "id": 23,
        "location": "Pasay",
        "restaurant_name": "The Food Truck at Sofitel",
        "status": "Open",
        "image_url": "https://secret-ph.com/wp-content/uploads/2023/03/3-47-768x402.jpg.webp"
    },{
        "id": 24,
        "location": "Paranaque, Metro Manila",
        "restaurant_name": "Nobu Restaurant",
        "status": "Closed",
        "image_url": "https://secret-ph.com/wp-content/uploads/2023/03/4-47-768x402.jpg.webp"
    },{
        "id": 24,
        "location": "Marikina, 1800 Metro Manila",
        "restaurant_name": "Rustic Mornings By Isabelo Garden",
        "status": "Open",
        "image_url": "https://secret-ph.com/wp-content/uploads/2023/03/5-46-768x402.jpg.webp"
    },{
        "id": 25,
        "location": "Paranaque, Metro Manila",
        "restaurant_name": "Loggia",
        "status": "Closed",
        "image_url": "https://secret-ph.com/wp-content/uploads/2023/03/6-44-768x402.jpg.webp"
    },{
        "id": 26,
        "location": "Makati, Metro Manila",
        "restaurant_name": "Spices at The Peninsula Manila",
        "status": "Open",
        "image_url": "https://secret-ph.com/wp-content/uploads/2023/03/7-46-768x402.jpg.webp"
    },{
        "id": 27,
        "location": "Manila",
        "restaurant_name": "Ilustrado",
        "status": "Open",
        "image_url": "https://secret-ph.com/wp-content/uploads/2023/03/8-44-768x402.jpg.webp"
    },{
        "id": 28,
        "location": "Kalakhang Maynila",
        "restaurant_name": "Talisay The Garden Cafe",
        "status": "Open",
        "image_url": "https://secret-ph.com/wp-content/uploads/2023/03/9-44-768x402.jpg.webp"
    },{
        "id": 29,
        "location": "Pasay, Metro Manila",
        "restaurant_name": "Apartment 1B at The Henry Hotel",
        "status": "Closed",
        "image_url": "https://secret-ph.com/wp-content/uploads/2023/03/10-43-768x402.jpg.webp"
    },{
        "id": 30,
        "location": "Metro Manila",
        "restaurant_name": "Cafe Ysabel",
        "status": "Closed",
        "image_url": "https://secret-ph.com/wp-content/uploads/2023/03/11-37-768x402.jpg.webp"
    },{
        "id": 31,
        "location": "Quezon City, Metro Manila",
        "restaurant_name": "Delgado.112",
        "status": "Open",
        "image_url": "https://secret-ph.com/wp-content/uploads/2023/03/12-35-768x402.jpg.webp"
    },{
        "id": 32,
        "location": "Sagada,Mountain Province",
        "restaurant_name": "Gaia Cafe & Crafts",
        "status": "Closed",
        "image_url": "https://secret-ph.com/wp-content/uploads/2023/10/1.-Gaia-Cafe-Crafts-1.jpg.webp"
    },{
        "id": 33,
        "location": "Sagada,Mountain Province",
        "restaurant_name": "Yoghurt House",
        "status": "Open",
        "image_url": "https://secret-ph.com/wp-content/uploads/2023/10/2.-Yoghurt-House.jpg.webp"
    },{
        "id": 34,
        "location": "Sagada,Mountain Province",
        "restaurant_name": "Sagada Brew",
        "status": "Open",
        "image_url": "https://secret-ph.com/wp-content/uploads/2023/10/3.-Sagada-Brew.jpg.webp"
    },{
        "id": 35,
        "location": "Sagada,Mountain Province",
        "restaurant_name": "Log Cabin",
        "status": "Closed",
        "image_url": "https://secret-ph.com/wp-content/uploads/2023/10/4.-Log-Cabin.jpg.webp"
    },{
        "id": 36,
        "location": "Sagada,Mountain Province",
        "restaurant_name": "Sagada Lemon Pie House",
        "status": "Open",
        "image_url": "https://secret-ph.com/wp-content/uploads/2023/10/5.-The-Sagada-Lemon-Pie-House.jpg.webp"
    },{
        "id": 37,
        "location": "Sagada,Mountain Province",
        "restaurant_name": "Caja Pizza, Cupcakes and more",
        "status": "Open",
        "image_url": "https://secret-ph.com/wp-content/uploads/2023/10/6.-Caja-Pizza-Cupcakes-and-more.jpg.webp"
    },{
        "id": 38,
        "location": "Poblacion, Sagada",
        "restaurant_name": "Masferre Country Inn and Restaurant",
        "status": "Closed",
        "image_url": "https://secret-ph.com/wp-content/uploads/2023/10/7.-Masferre-Country-Inn-and-Restaurant.jpg.webp"
    },{
        "id": 39,
        "location": "Sagada,Mountain Province",
        "restaurant_name": "Sagada Cellar Door",
        "status": "Closed",
        "image_url": "https://secret-ph.com/wp-content/uploads/2023/10/8.-Sagada-Cellar-Door.jpg.webp"
    },{
        "id": 40,
        "location": "Sagada,Mountain Province",
        "restaurant_name": "Ramyun Restobar",
        "status": "Open",
        "image_url": "https://secret-ph.com/wp-content/uploads/2023/10/9.-Ramyun-Restobar.jpg.webp"
    },{
        "id": 41,
        "location": "Banaue, Ifugao",
        "restaurant_name": "Hagabi Restaurant",
        "status": "Closed",
        "image_url": "https://secret-ph.com/wp-content/uploads/2023/06/1.-Hagabi-Restaurant.jpg.webp"
    },{
        "id": 42,
        "location": "Sagada,Mountain Province",
        "restaurant_name": "Rust n Wood",
        "status": "Open",
        "image_url": "https://secret-ph.com/wp-content/uploads/2023/10/10.-Rust-n-Wood.jpg.webp"
    },{
        "id": 43,
        "location": "Lamut, Ifugao",
        "restaurant_name": "Dindos Restaurant",
        "status": "Open",
        "image_url": "https://secret-ph.com/wp-content/uploads/2023/06/2.-Dindos-Restaurant.jpg.webp"
    },{
        "id": 44,
        "location": "Lagawe, Ifugao",
        "restaurant_name": "The Riverview Restaurant",
        "status": "Closed",
        "image_url": "https://secret-ph.com/wp-content/uploads/2023/06/3.-The-Riverview-Restaurant.jpg.webp"
    },{
        "id": 45,
        "location": "Banaue, 3601 Ifugao",
        "restaurant_name": "Uyamis Green View Lodge and Restaurant",
        "status": "Open",
        "image_url": "https://secret-ph.com/wp-content/uploads/2023/06/4.-Uyamis-Green-View-Lodge-and-Restaurant.jpg.webp"
    },{
        "id": 46,
        "location": "Lagawe, Ifugao",
        "restaurant_name": "Gazebo",
        "status": "Closed",
        "image_url": "https://secret-ph.com/wp-content/uploads/2023/06/5.-The-Gazebo.jpg.webp"
    },{
        "id": 47,
        "location": "Lamut, Ifugao",
        "restaurant_name": "Kings Restaurant",
        "status": "Open",
        "image_url": "https://secret-ph.com/wp-content/uploads/2023/06/6.-Kings-Restaurant.jpg.webp"
    },{
        "id": 48,
        "location": "Banaue, 3601 Ifugao",
        "restaurant_name": "Als Place Banaue Ifugao",
        "status": "Open",
        "image_url": "https://secret-ph.com/wp-content/uploads/2023/06/7.-Als-Place-Banaue-Ifugao.jpg.webp"
    },{
        "id": 49,
        "location": "Banaue, Ifugao",
        "restaurant_name": "Batad Pension Restaurant",
        "status": "Closed",
        "image_url": "https://secret-ph.com/wp-content/uploads/2023/06/10.-Batad-Pension-Restaurant.jpg.webp"
    },{
        "id": 50,
        "location": "Banaue, 3601 Ifugao",
        "restaurant_name": "Banaue -View Cafe",
        "status": "Open",
        "image_url": "https://secret-ph.com/wp-content/uploads/2023/06/8.-Banaue-View-Cafe.jpg.webp"
    },
]


@app.route('/')
def hello_world():
    print(restaurants);
    return render_template('index.html', restaurants=restaurants)

if __name__ == '__main__':
    app.run(debug=True)