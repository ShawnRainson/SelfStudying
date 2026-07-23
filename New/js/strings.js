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
    text.replace(text[0], text[0].toUpper());
    return text;
    //Не знаю как реализовать, объясни
}

function replaceSpaces(text) {
    newSpace = text.replace(" ", "_");
    return newSpace;
}

function containsWord(text, word) {
    splittedText = text.split();
    if (word in splittedText) {
        return true;
    } else {
        return false;
    }
}

word = countLetters("bear");
console.log(`Letters count: ${word}`);
space_count = countSpaces("Hello world dude!");
console.log(`Spaces count: ${space_count}`);
changeSpace = replaceSpaces("Hello world!");
console.log(changeSpace);
checkWord1 = containsWord("Hello world!", "Hello");
checkWord2 = containsWord("Hello world!", "python");
console.log(`First word: ${checkWord1}`);
console.log(`Second word: ${checkWord2}`);
//newWord = capitalize("program");
//console.log(newWord);

//Не знаю как сделать реверс, а в поиске слова в тексте, я знаю как сделать, но как бы не пытался не работает, помоги пожалуйста
