function reversePrint(){
    for (let i=1;i<=7;i+=2){
        let newStr=''
        for(let j=1;j<=i;j++){
            newStr+='*'
        }
        console.log(newStr)
    }
}

reversePrint()
