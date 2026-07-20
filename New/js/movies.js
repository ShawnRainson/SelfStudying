const movies = [
    {
        title: "Avatar",
        year: 2009,
        rating: 9.2
    },
    {
        title: "Interstellar",
        year: 2014,
        rating: 9.7
    }
];

function showMovies(movieList) {
    for(let obj of movieList) {
        console.log(`${obj.title} (${obj.year}) - ${obj.rating}`);
    }
}

function findMovie(movieTitle, movieList) {
    let found = false;
    for(let checkTitle of movieList){
        if (checkTitle.title === movieTitle) {
            console.log(`Movie: ${checkTitle.title}`);
            found = true;
            break;
        };
    }
    if (found === false) {
        console.log("Movie not found");
    }
}

function addMovie(movie, movieList) {
    movieList.push(movie);
}

showMovies(movies);
findMovie("Avatar", movies);
findMovie("Monster house", movies);
addMovie({title: "Spider man", year: 2002, rating: 9.1}, movies);
showMovies(movies);
