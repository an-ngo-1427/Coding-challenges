function printZeros(){
    for (let i=0;i<4;i++){
        for (let j=0;j<4;j++){
            if(j==i) console.log('1')
            else console.log('0')
        }
        console.log('\n')
    }
}

printZeros()
