function countLetters(text) {
    let counter = 0;
    for(let letter of text) {
        counter++;
    }
    return counter;
}

function countSpaces(text) {
    let counter = 0;
    for(let space of text) {
        if(space === " ") {
            counter++;
        }
    }
    return counter;
}

function capitalize(text) {
    //Не знаю как реализовать
}

word = countLetters("bear");
console.log(`Letters count: ${word}`);
space_count = countSpaces("Hello world dude!");
console.log(`Spaces count: ${space_count}`);
newWord = capitalize("program");
console.log(newWord);