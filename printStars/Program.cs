// See https://aka.ms/new-console-template for more information


    //  void printFunc(int[] arr){
    //     for(int i=arr.Length-1;i>=0;i--){
    //         Console.Write(arr[i]);
    //     }
    //     Console.Write("/n");
    // }

    // printFunc([1,2,3,4]);

    void reverseArr(int[] arr){
        int i =0;
        int j = arr.Length-1;
        while(i < j){
            (arr[i],arr[j]) = (arr[j],arr[i]);
            i++;
            j--;
        }
        Console.WriteLine(arr);

    }

    reverseArr([1,2,3,4]);
