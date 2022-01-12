//const request = require("request-promise")
//const cheerio = require("cheerio")
//https://api.binance.com/api/v3/ticker/price

import stringify from 'fast-json-stable-stringify';
import fetch from 'node-fetch';

async function getData(){
    const response = await fetch('https://api.binance.com/api/v3/ticker/price');
    const allCoins = await response.text();
    var obj = await JSON.parse(allCoins);
    //console.log(obj); //print to console
    for(var i in obj){
        console.log(obj[i].symbol);
    }
}



getData()




//.catch(err => console.error(err)); 