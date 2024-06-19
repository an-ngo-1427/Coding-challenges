// See https://aka.ms/new-console-template for more information

int MaxAreaOfIsland(int[][] grid) {

        int maxArea = 0;
        HashSet<(int,int)> uniquePairs = new HashSet<(int,int)>();
        List<(int,int)> neighBors = new List<(int,int)>();

        for(int i=0;i<grid.Length;i++){
            for(int j=0;j<grid[i].Length;j++){
                int totalArea = 0;
                if(uniquePairs.Contains((i,j))){
                    continue;
                }
                if(grid[i][j] == 1 && !uniquePairs.Contains((i,j))){
                    neighBors.Add((i,j));
                    uniquePairs.Add((i,j));
                    totalArea++;
                }
                while(neighBors.Count >0){
                    (int, int) curr = neighBors[neighBors.Count - 1];
                    int x = curr.Item1;
                    int y = curr.Item2;
                    neighBors.RemoveAt(neighBors.Count - 1);
                    // top neighbor
                    if( x > 0 && grid[x-1][y] == 1 && !uniquePairs.Contains((x-1,y))){
                        neighBors.Add((x-1,y));
                        uniquePairs.Add((x-1,y));
                        totalArea++;
                    }
                    // bottom neighbor
                    if( x < grid.Length - 1 && !uniquePairs.Contains((x+1,y)) && grid[x+1][y] == 1){
                        neighBors.Add((x+1,y));
                        uniquePairs.Add((x+1,y));
                        totalArea++;
                    }
                    // left neighbor
                    if( y > 0 && !uniquePairs.Contains((x,y-1)) && grid[x][y-1]==1 ){
                        neighBors.Add((x,y-1));
                        uniquePairs.Add((x,y-1));
                        totalArea++;
                    }
                    //right neighbor
                    if( y < grid[x].Length - 1 && !uniquePairs.Contains((x,y+1)) && grid[x][y+1]==1){
                        neighBors.Add((x,y+1));
                        uniquePairs.Add((x,y+1));
                        totalArea++;
                    }
                    // removing last element in neighBors

                }
                if(totalArea > maxArea){
                    maxArea = totalArea;
                }
            }

        }
        return maxArea;
    }



    int[][] grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]];
    int[][] grid1 = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0]];
    MaxAreaOfIsland(grid1);
