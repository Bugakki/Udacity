import media
import fresh_tomatoes

ShawshankRedemption = media.Movie("Shawshank Redemption",
                        "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
                        "https://images-na.ssl-images-amazon.com/images/I/519NBNHX5BL._SY445_.jpg",
                        "https://www.youtube.com/watch?v=NmzuHjWmXOc")

DarkKnight = media.Movie("The Dark Knight",
                         "When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham, the Dark Knight must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
                         "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                         "https://www.youtube.com/watch?v=EXeTwQWrcwY")

#ShawshankRedemption.show_trailer()

Inception = media.Movie("Inception",
                        "A thief, who steals corporate secrets through the use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0")


HotelTransylvania = media.Movie("Hotel Transylvania",
                                "Dracula, who operates a high-end resort away from the human world, goes into overprotective mode when a boy discovers the resort and falls for the count's teenaged daughter.",
                                "https://vignette.wikia.nocookie.net/hoteltransylvania/images/6/68/Hotel-Transylvania-06.jpg/revision/latest?cb=20120911203200",
                                "https://www.youtube.com/watch?v=q4RK3jY7AVk")


ShutterIsland = media.Movie("Hotel Transylvania",
                                "In 1954, a U.S. Marshal investigates the disappearance of a murderer, who escaped from a hospital for the criminally insane.",
                                "https://s3-ap-southeast-2.amazonaws.com/fna-wordpress-website06/wp-content/uploads/2016/11/26021839/Shutter-Island-1440x960.jpg",
                                "https://www.youtube.com/watch?v=5iaYLCiq5RM")


LORD = media.Movie("The Lord of the Rings",
                                "A meek Hobbit from the Shire and eight companions set out on a journey to destroy the powerful One Ring and save Middle-earth from the Dark Lord Sauron.",
                                "https://images-na.ssl-images-amazon.com/images/M/MV5BN2EyZjM3NzUtNWUzMi00MTgxLWI0NTctMzY4M2VlOTdjZWRiXkEyXkFqcGdeQXVyNDUzOTQ5MjY@._V1_UX182_CR0,0,182,268_AL_.jpg",
                                "https://www.youtube.com/watch?v=V75dMMIW2B4")

movies = [ShawshankRedemption,DarkKnight,Inception,HotelTransylvania,ShutterIsland,LORD]
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.__doc__)
