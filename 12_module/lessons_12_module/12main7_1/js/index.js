//12main7_1
//Циклы JavaScript
//for,while,do while

//цикл for
//сначало делаем пер-ую,потом говорим до когда цикл будет идти(условие)
//и потом что делаем с пер-ой(плюсуем к i единицу)
//если в одну строчку,то {} можно не ставить


// for(var i = 0; i < 10; i++){
//     console.log(i);
// }
// for(var i = 100; i > 10; i-=10){
//     console.log(i);
// }

//цикл while

let i = 0; //надо создавать пер-ую вне цикла
while(i < 10){
    console.log(i);
    i++;
}
let j = 1;
while(j <= 100){
    console.log(j);
    j *= 2;
}

//do while - тоже самое что while,только сначало он выполнится,а потом проверит условие
//если условие не верно,он остановится


var l = 100;
do{
    console.log(l);
    l++;
}while(l<10);

//операторы break,continue

for(var c = 100; c > 10; c/=2){
    if(c<25) //если с<50 выходим из цикла
    break;
    console.log(c);
}
// если прописать проверку в конце,то и код будет выполняться сверху вниз
//разные выводы получаются в зависимости от задачи надо смотреть где лучше прописывать проверку


//оператор continue:
for(var v = 1; v < 20; v++){
    if(v>15)
    break;
    if (v % 2 !=0)
        continue;
    console.log(v);
}

// создадим массив для практики над циклами

let arr = [5,6,"Hello",'s',true,9];

for(var b = 0; b < arr.length; b++){
    console.log("Элемент под номером №" + (b+1) + ": " + arr[b]);
}
console.log("");

var n = 0;
while(n < arr.length){
    console.log("Элемент c номером №" + (n+1) + ": " + arr[n]);
    n++;
}

//for и while не лучшие циклы для работы с массивами
//для этого лучше исп-ть forEach (он и был изобретен для работы с массивами)
//указываем массив,затем forEach,затем function(1 пар-тр - опр-ый эл-нт в массиве,индекс,название массива)

arr.forEach(function(item,m,array){
    console.log("Элемент c номером №" + m + ": " + item + ".Массив: " + array);
});

//for in - для перебора обьектов

for(var key in arr){
    console.log("Элемент c номером №" + key + ": " + arr[key]);
}

//разница между let и var
//область видимости var видно вне цикла(ф-ии?).let не видно(выбивает ошибку)

for(var a = 0;a < 10; a++)
    console.log(a);

console.log(" ");

console.log(a);

for(let s = 0;s < 10; s++)
    console.log(a);

console.log(" ");

console.log(s);