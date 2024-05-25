//URL:https://leetcode.com/problems/rotate-image/description/
var rotate = function (matrix) {
    let n = matrix.length;
    let arr = JSON.parse(JSON.stringify(matrix));
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            matrix[i][j] = arr[n - 1 - j][i];
        }
    }
    return matrix;
};
