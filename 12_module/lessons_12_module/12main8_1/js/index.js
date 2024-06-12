//12main8_1
//Функции для массивов(ForEach,Filter,Map,Reduce)

//ф-я forEach(выбивает ошибку не находит forEach)
let arr = ["BMW","Mersedes","Audi","Volvo"];

//чтобы перебрать можно ис-ть For и While,но лучше ForEach
//сначало указываем массив,далее ф-цию,далее прописываем оп-ю ф-ю
//в ней указываем 3 пар-ра(сам эл-нт кот. перебираем,индекс,массив с кот.работаем)

arr.forEach(function(item,i,arr){
    console.log("Index:" + i + ": " + item + ". Массив: " + arr);
});


//ф-я filter - фильтрует массив,даем один массив,а получаем другой,отфильтрованый
//условие:берем те эл-ты у кот. длинна строки либо 3 либо 4 символа
//тоже не работает


let newArr = arr.filter(function(el) {
    //всегда пишем,т.к. возвращать будем отфильтрованый массив
    return el.length == 3 || el.length == 4;
});

console.log(newArr);

var arr_2 = [1,-1,2,3,-3];
var positive = arr_2.filter(function(el){
    return el < 0;
});
console.log(positive);

//ф-я map - для трансформации каждого эл-та(перебирает все эл-ты,и возвращает все
//элементы,только те что не в входят в фильтр все равно будет вписывать в новый массив
//по значением undefined)
//toLowerCase - перевод в нижний регистр

let newArr2 = arr.map(function(el){
    if(el.length == 3)
    return el.toLowerCase();
});
console.log(newArr2);


//ф-я every и some
//если длинна эл-та равна 3,возвращаем True,иначе False
function elLength(el) {
    return el.length == 3;
}
//не добавляем круглые скобки после elLength,т.к. она сразу будет выполняться
console.log(arr.every(elLength));//возвращает False(если для каждого эл-та в массиве 
//условие будет True,она вернет True)
console.log(arr.some(elLength));//возвращает True(если хотя бы 1 эл-нт
//попадает под это условие,вернет True)

//ф-я reduce - все эл-ты просматриваем слева направо,reduce right - справа на лево

let nums = [1,2,3,4,5];
//sum - в этот пар-тр будет записываться сумма всех эл-тов
//el - текущий эл-нт этого массива
let summa = nums.reduce(function(sum,el){
    return sum + el;
});
console.log(summa);

//среднее арифметическое

let currency = [23.5,4.56,33.5];
//total - работает с общей суммой
//el - с каждым отдельным эл-том
//index - отвечает за индекс каждого эл-та
//array - отвечает за весь массив с которым работаем
let average = currency.reduce(function(total,el,index,array){
    total += el; //в сумму добавляем текущий эл-нт
    if(index == array.length - 1) //проверяем является ли эл-нт последним
        return total/array.length;
    else
        return total;
});

console.log(average);

//ф-я reduceRight
//все тоже же самое,но сконца массива

//let currency2 = [23.5,4.56,33.5];
let currency2 = [];
let average2 = currency2.reduceRight(function(total,el,index,array){
    total += el;
    //if(index == array.length - 1)//теперь это условие не срабатывает,
    //чтобы срабатывало надо проверить на index=0
    if(index ===0)
        return total/array.length;
    else
        return total;
//в эти ф-ии можно устанавливать второй пар-тр(по умолчанию)-сработает,
//если массив будет пустой например
},0);

console.log(average2);