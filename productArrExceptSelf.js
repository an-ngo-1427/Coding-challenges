function productExceptSelf(nums){
    const n = nums.length;
    let pre = []
    let suff = new Array(n)
    pre[0] = 1
    suff[n-1] = 1;

    for(let i=1;i<n;i++){
        pre[i] = pre[i-1] * nums[i-1]
        console.log(pre)
    }

    for(let i = n - 2; i >= 0; i--) {
        suff[i] = suff[i + 1] * nums[i + 1];
        console.log(suff)
    }

    let ans = []
    for(let i = 0; i < n; i++) {
        ans[i] = pre[i] * suff[i];
    }
    console.log('answer',ans)
}

productExceptSelf([1,2,3,4])
