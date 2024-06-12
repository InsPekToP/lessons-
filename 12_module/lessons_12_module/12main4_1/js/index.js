//12main4_1
//Операторы
//создаем папку vars.js
//теперь в index.html подключам vars.js (<script src = "js/vars.js"></script>)
//теперь можем обращаться ко всем переменным в файле vars.js

//console.log(mySecond);
//важна последовательность.Сначало подключаем vars.js(пер-ные).А потом обращаемся к ним:
/* <script src = "js/vars.js"></script>
    <script src="js/index.js"></script> */

//математические операторы

var x = 5;
var y = 10;
var res;

res = x + y;
console.log('Результат: ' + res);

res = x - y;
console.log('Результат: ' + res);

res = x * y;
console.log('Результат: ' + res);

res = x / y;
console.log('Результат: ' + res);

res = x % y; //остаток при делении
console.log('Результат: ' + res);

//Сокращ. математ действия

res = res +5;
console.log('Результат: ' + res);

res -= 5; //тоже самое.(*= /= -=) - с остальными действиями тоже работает
console.log('Результат: ' + res);

res++; //добавили 1.(--) - уменьшаем на 1
console.log('Результат: ' + res);

res = -res; //унарный минус(меняет знак перед числом)
console.log('Результат: ' + res);

var a = 5;
res = a + y*2; //работают стандартные законы математики
console.log('Результат a: ' + res);

//обьединение строк
var w1 = 'hello';
var w2 = 'world';
console.log(w1+w2);

//числа преобразуются в строки,если писать вместе со строками
console.log('Результат a: ' + a + y); 
//чтобы этого не было,надо прописать в скобках
console.log('Результат a: ' + (a + y));