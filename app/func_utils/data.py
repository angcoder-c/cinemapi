from app.models import User, Movie, Function, Ticket

show_1 = Function(1, '2022-12-31 19:10:00', 'KJSD', 1)
show_1.id_A01=1

show_2 = Function(2, '2022-11-19 18:30:00', 'ABCD', 2)
show_2.id_A02=2

show_3 = Function(3, '2022-11-19 22:00:00', 'XYZC', 3)
show_3.id_A03=3

show_4 = Function(4, '2022-11-20 12:50:00', 'BDBR', 1)
show_4.id_A04=4

show_5 = Function(5, '2022-11-20 14:05:00', 'OQWI', 3)
show_5.id_A05=5

data = [
    User('User', 'Admin', 'useradm', 'admin123', 'useradm@email.com', '12345678', '502'),
    User('Joe', 'Miller', 'joemlr', '123', 'joe@email.com', '91011121', '502'),
    User('Michael', 'Scott', 'michaelscott', '123', 'michael@email.com', '31415161', '502'),
    User('Ryan', 'Howard', 'ryanhwd', '123', 'ryan@email.com', '71819202', '502'),
    User('Jim', 'Halpert', 'jimhpt', '123', 'jim@email.com', '12223242', '502'),
        
    Movie(
        'Harry potter and the philosophers stone', 
        'https://cdn.shopify.com/s/files/1/0057/3728/3618/products/108fdcc83e78192f1bd2084709a2e7d1_71580467-f819-4a5e-87b0-94b412bbc81a_480x.progressive.jpg?v=1573593624', 
        'https://www.youtube.com/watch?v=ZgrCZVjPg9g', 
        'PG'
    ),
    Movie(
        'Star Wars: Episode IV - A New Hope', 
        'https://cdn.shopify.com/s/files/1/0057/3728/3618/products/6cd691e19fffbe57b353cb120deaeb8f_8489d7bf-24ba-4848-9d0f-11f20cb35025_480x.progressive.jpg?v=1573613877', 
        'https://www.youtube.com/watch?v=beAH5vea99k', 
        'PG'
    ), 
    Movie(
        'The lord of the rings the fellowship of the ring', 
        'https://cdn.shopify.com/s/files/1/0057/3728/3618/products/b1b6860c465f64983d81a2ce14019d7e_cb04f573-c07e-4fc4-af7d-72fcb83623d6_480x.progressive.jpg?v=1573588822', 
        'https://www.youtube.com/watch?v=V75dMMIW2B4', 
        'PG-13'
    ), 
    Movie(
        'The Social Network', 
        'https://cdn.shopify.com/s/files/1/0057/3728/3618/products/2b3adf28f07240c40a9ba5f2bd01df3f_1776be06-81df-4a1e-85e6-146ff6513eb0_480x.progressive.jpg?v=1573593770', 
        'https://www.youtube.com/watch?v=2RB3edZyeYw', 
        'PG-13'
    ), 
    Movie(
        'Enders Game', 
        'https://cdn.shopify.com/s/files/1/0057/3728/3618/products/613fb4a8fa84396178402aac9c20871d_4475ad1e-8335-4ca6-93fe-f62b2ee40055_480x.progressive.jpg?v=1573618954', 
        'https://www.youtube.com/watch?v=2SRizeR4MmU', 
         'PG-13'
    ),

    show_1,
    show_2,
    show_3,
    show_4,
    show_5,

    Ticket(1, 1, 1),
    Ticket(2, 2, 2),
    Ticket(3, 3, 3),
    Ticket(4, 4, 4),
    Ticket(5, 5, 5)
]

