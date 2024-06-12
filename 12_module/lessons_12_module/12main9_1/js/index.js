//12main9_1
//Коллекции Set и Map

//Set - не может быть повторяющихся эл-тов

let mySet = new Set(); //создаем обьект на основе класса Set()
//new - выделяем память

mySet.add(5);
mySet.add(5.4);
mySet.add("5");
mySet.add({"name":"Alex"});
mySet.add(55);
mySet.add(true);

mySet.delete(5); //удаление эл-та
console.log(mySet.has(5)); //есть ли в массиве 5-ка(false или true)

mySet.add(5);//его уже нельзя добавить(не выводится в консоль)
console.log(mySet.has(5)); 

console.log(mySet);//для вывода в консоль,лучше ис-ть цикл

for(let el of mySet) //off - вместо in.Внутри какой коллекции надо перебирать
    console.log(el);

//так же можно перебирать и через остальные циклы:forEach и т.д.

mySet.forEach(function(el){
    console.log(el);
});

//коллекция map - можем сохранять эл-ты в формате ключ:значение
//разница с обьектом в том,что в обьекте все преобразуется в строку("1":Алекс)
//а для коллекции map можем передовать различные типы данных

let map = new Map();
map.set("first","str1");//set-фунция,получает 2 пар-ра(ключ:значение)
map.set(2,"str2");
map.set(true,"str3");
map.set({"name":"alex"},"str4"); //в качестве ключа можно ук-ть полноценные обьекты {}

//map.delete(2);//удаляем эл-нт у кот. ключ со знач. 2
console.log(map.size);//длинна всей кол-ии
console.log(map.has(2));//есть ли ключ 2

console.log(map);

//keys - ф-я позволяет получить доступ к ключам
for(let i of map.keys())
    console.log(i);

//values - получить значение
for(let i of map.values())
    console.log(i);

//и ключи и значения(вообще ничего не пишу)
for(let i of map)
    console.log(i);

for(let i of map)
    console.log(i[0]);//ключи

for(let i of map)
    console.log(i[1]);//значения
//Коллекция map - тоже самое что и обьекты,только в качестве ключа можно
//устанавливать любой тип данных