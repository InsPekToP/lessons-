//12main13_1
//JSON в JavaScript
//JSON - спец. формат данных,которыйй представляет из себя какой либо обьект
//Способ ощаться между разными языками програмирования

//создание обычного обьекта
//в JSON стандарте обьект создается с ис-ем {}
//чтобы это все стало JSON обьектом,надо обернуть это все в ''(тоесть стала строкой)
let obj = '{"name":"Alex","age":45,"hasCar":true}';

//чтобы из стоки(JSON) сделать стандартный обьект:
obj = JSON.parse(obj);

console.log(obj.name);//не работает,т.к. это теперь строка(работает после преобразования)
console.log(obj);


//также можно это делать и с массивами
let array = '[56,7,2,89]';
array = JSON.parse(array);
console.log(array);

//также и в обратную сторону работает(из обьекта в строку)
obj = JSON.stringify(obj);
console.log(obj);

array = JSON.stringify(array);
console.log(array);

//также можно работать и со сложными обьектами(где знач. это массив данных)

let obj2 = '{"name":"Андрей","state":"USA","male":true,"friends":[0,1,2,3]}';
obj2 = JSON.parse(obj2);
console.log(obj2);
console.log(obj2.friends[1]);

//разница между JavaScript обьекта и JSON обьекта(В JSON обьекте строгая типизация)
//в JavaScript обьекте все написано правильно:
var objectJS = {
    name:"Андрей",
    "age":45,
    "state":'UA'
};
//но для JSON обьекта это все будет ошибочным("" долны быть на name и на UA)
var objectJSON = {
    name:"Андрей",//если не ставить "",то JSON подставит сам
    "age":45,
    "state":"UA"
};

//Теперь обратно(из обьекта в JSON формат)
let str = JSON.stringify(objectJSON,["name","state"],4);// 2й пар-тр говорит какие ключи будем добавлять
//3й пар-тр указывает кол-во пробелов слева
console.log(str);