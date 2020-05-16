class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor) {
        int oldColor = image[sr][sc];
        colorfill(image, sr, sc, oldColor, newColor);
        return image;
    }

private:
    void colorfill(vector<vector<int>>& image, int i, int j, int oldColor, int newColor){
            int m = image.size(), n = image[0].size();
            
            if(i < 0 || i == m || j < 0 || j == n || image[i][j] == newColor || image[i][j] != oldColor) return;
            
            image[i][j] = newColor;
            colorfill(image, i+1, j, oldColor, newColor);
            colorfill(image, i-1, j, oldColor, newColor);
            colorfill(image, i, j+1, oldColor, newColor);
            colorfill(image, i, j-1, oldColor, newColor);
    }
};