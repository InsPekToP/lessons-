//12main10_1
//Функциии - небольшие подпрограмки с повторяющимся кодом

function show() {
    console.log("Hello World");
}

//ф-ии всегда нужно вызывать(можно несколько раз)
show();
show();
show();

//в ф-ях существует понятие локальные и внешние пер-ные
//создали в ф-ии пер-ную el - локальная

var i = 0; //внешняя пер-ная(теперь можем вывести во всех ф-ях)


function show2() {
    var el = "Element";
    console.log("\n" + el + i);
}

function print() {
    var el2 = "Буй";
    console.log("\n" + el2 + i);
}


show2();
print();
//теперь пытаемся к ней обратиться вне этой ф-ии(будет ошибка)
// console.log(el);
console.log(i);

//ф-ии могут принимать и не принимать пар-ры.

function calc(a,b) {
    if(b == undefined)//можем проверить на undefined
    b=10;
    var res = a+b;
    console.log(res);
}


//можно вызывать ф-ю не передавая в нее пар-ры
calc(56,6);
calc(56);//если не передавать 2й пар-тр,то будет undefined

//также ф-ии могут возвращать какие-либо значения
//отличие:если выводить пре-ую,то она просто выводится в консоли(например)
//если возвращать,то эту пер-ную можем записать в другую пер-ую

function multiply(a,b,c){
    var res = a*b*c;
    return res;
}
//multiply(5,2,2);//теперь ничего не вывелось,т.к. return он возвращает рез-тат

let mult = multiply(5,2,2);//теперь в пер-ую mult будет записана пер-ая res,
//а в пер-ую res будет записано 5*2*2
console.log(mult);

//нахождение четного числа в массиве
function arrayEven(array){
    let isEven = true;//создали пер-ную
    array.forEach(function(item,i,arr){//перебираем массив
        if(item %2 !=0)//если эл-нт не четный
            isEven=false;//применяем isEven=false
    });
    return isEven;//возвращаем isEven
}

let arr = [5,9,0,4];
let arr_2 = [6,8,0,4];

let isEven = arrayEven(arr);
console.log(isEven);//выдает false,т.к. есть нечетные эл-ты

let isEven2 = arrayEven(arr_2);
console.log(isEven2);//выдает true,если все эл-ты четные

//для ф-ий с пар-ми можно устанавливать знач. по умолчанию

function calc2(a=12,b=10) {//устанавливаем знач. по умолчанию
    // if(b == undefined)//можем сократить эти 2 строчки,прописав сразу присоздании пер-ой
    // b=10;
    var res = a+b;
    console.log(res);
}
calc2();
//также ф-ию можно записать в пер-ую
let func = calc2; //круглые скобки ставить не надо,т.к. она сразу вызовется,
//а надо чтобы она просто переписалась в новую пер-ную

func(5,10);//теперь можем вызывать пер-ную как ф-ю
func = null;//очищаем пер-ую(становится пустой)

//2й способ из пер-ой делать ф-ию
let func2 = function(mess = "Боб"){//нет названия и ставится ;
    console.log("Привет:"+mess);
};
func2();
func2("Алекс");
//разница в том,что во 2м способе мы не можем вызвать ф-ию до ее обьявления


//Можно создать ф-ию,кот. будет выполнена с задержкой по времени
function test(){
    console.log("Hello world");
}
setTimeout(test,1500); //встроенная ф-я(принимает 2 пар-ра(саму ф-ию,время в м/с))

//можно передовать пар-тр в test2,тогда 3 пар-тр в setTimeout можно передавать этот пар-тр.И т.д.
function test2(words){
    console.log(words);
}
setTimeout(test2,2000,"Hello");

//сущ-ет несколько вар-ов записи setTimeout(записывается маленький кусочек JS)
setTimeout("console.log('Хай')",2500);

setTimeout(function(){
    console.log('Привет')
},3000);

//можно отменить выполнение setTimeout
let timeOut = setTimeout(function(){
    console.log('Хелоу')
},3500);
clearTimeout(timeOut);//отмена setTimeout(принимает 1 пар-тр(пер-ая))

//ф-я создающая таймер
//setInterval(test2,2000,"setInterval");//через каждые 2 сек выводит в консоль setInterval

let interval = setInterval(function(){
    console.log('Приветики');
},2000);

//через 10 секунд очищаем ф-ию
setTimeout(function(){
    clearInterval(interval);
    console.log("Стоп");
},10000);

