//12main5_1
//Условные операторы - проверяет работает ли условие

let x = 20;
let y = 20;

let hasCar = true;

// if (x==y) { //если х равен у
//     console.log("Числа равны")
// }
//if (x!=y) { //если х не равен у
    //console.log("Числа не равны"); // ; надо писать,но если не писать ошибки не будет
//так же можно проверять на < > <= >=
//}
//else{
    //console.log("Числа равны");
//можно пропуcкать фигурные скобки,если писать только одну строчку кода
//}


//оператор else if - не является обязательным пар-ом
if (x>y){
    console.log("Число Х больше чем чило У");
    console.log("Проверка");
}else if (x==y){
    console.log("Числа равные");

    if(x != 25){ // также можно прописывать проверку в проверке
        console.log("Число Х не равно 25");
    }
    //&& - и
    // || - или
    // hasCar == true и hasCar - одно и тоже
    // hasCar == false и !hasCar - тоже самое
    if(x != 24 || (hasCar == true && y == 24)){
        console.log("Число Х не равно 24");
    }
}else if (x==20){
    console.log("Число Х равно 20");
}else if (x==26){
    console.log("Числа Х равно 26");
}
else{
    console.log("Числа не равны");
}

//Операторы switch - case - проверка на опр-ые условия
//фигурные скобки обязательны
//break - тоже надо писать,чтобы выходить из итерации
//defol - тоже,что и else - выполняется,если прошлые комманды не были выполнены(можно
//не ставить break,т.к. этот оператор пишется в конце,но лучше ставить


//let str = "George";
// let str = "Petr";
//let str = "Some-1";
let str = "Some-2";


switch(str){
    case "John":
        console.log("Имя John")
        break;
    case "Bob":
        console.log("Имя Bob");
        break;
    case "George":
        console.log("Имя George");
        break;
//если не ставить опер-тор break - выводится и Petr и Alex - Т.к. не 
//выходим из проверки,дальше идет case "Alex": - это просто проверка,
//он с ней ничего не делает и пропускает,поэтому выводит console.log("Имя Alex");
//а затем доходит до break и выходит из итерации.
    case "Petr": 
        console.log("Имя Petr");
        break;
    case "Alex":
        console.log("Имя Alex");
        break;
//пропуск break можно исп-ть,когда нужно проверить на несколько соответсвий
    case "Some-1":
    case "Some-2":
    case "Some-3":
    case "Some-4":
        console.log("Some");
        break;
    default:
        console.log("Нам не известно имя");
        break;
    }

//тернарные операторы - сокращение if else
//это:

let nums = 23;
let res = "";
if(nums > 25)
    res = "Big";
else
    res = "Small";
console.log(res);

//тоже самое что и это:
//? - проверка, : - заменяет if else
let result = nums > 25 ? "Big":"Small";
console.log(result);