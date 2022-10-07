package Q1;

public class Matrix {
    private int n,m ;
    private int mat[][] ;

    Matrix(int n, int m, int v) {
        /* 
         * TODO: Complete this constructor
         * Initialize a matrix of size n x m with all elements equal to v
         */ 
        this.n =n;
        this.m =m;
        mat=new int[n][m];
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                mat[i][j]=v;
            }
        }
    }

    Matrix(int n, int m) {
        /* 
         * TODO: Complete this constructor 
         * Initialize a matrix of size n x m with all elements equal to 0
         */
         this.n =n;
        this.m =m;
         mat=new int[n][m];
         for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                mat[i][j]=0;
            }
        }
    }

    static Matrix add(Matrix A, Matrix B) {
        /*
         * TODO: Complete this method
         * Add two matrices and return the result
         * and return a zero matrix of size 1 x 1
         */
         if(A.getrows()!=B.getrows() || A.getcols()!=B.getcols()){
            Matrix zero = new Matrix(1,1);
            zero.mat[0][0]=0;
            return zero;
         }
         else{
          Matrix matr = new Matrix(A.getrows(),A.getcols()) ;
         for(int i=0; i<A.getrows(); i++){
            for(int j=0; j<A.getcols(); j++){
                matr.mat[i][j]=A.mat[i][j]+B.mat[i][j];
            }
         }
         return matr;
         }
    }

    static Matrix matmul(Matrix A, Matrix B) {
        /*
         * TODO: Complete this method
         * Multiply two matrices and return the result
         * and return a zero matrix of size 1 x 1
         */
         if(A.getcols()!=B.getrows()){
            Matrix zero = new Matrix(1,1);
            zero.mat[0][0]=0;
            return zero;
         }
         else{
         Matrix mult = new Matrix(A.getrows(),B.getcols());
        int i= 0 ;
        int sum=0;
        int k=0;
        int j;
	    while( i < A.getrows() )
         {
        
             j= 0 ;
	        while( j <B.getcols())
          	   {
 		        sum=0;
                k=0; 
		        while(k <B.getrows())
  		        {
                sum +=A.mat[i][k]*B.mat[k][j]   ;
		        k++ ;
                }
                mult.mat[i][j]=sum;
                j++;
                }
            i++;
        }
         return mult;
         }
    }

    void scalarmul(int k) {
        /*
         * TODO: Complete this method
         * Multiply all elements of the matrix by k
         */
         for(int i=0; i<mat.length; i++){
            for(int j=0; j<mat[0].length; j++){
                mat[i][j]=k*mat[i][j];
            }
         }
    }

    int getrows() {
        /*
         * TODO: Complete this method
         * Return the number of rows in the matrix
         */
         int rows;
         rows= mat.length;
         return rows;
    }

    int getcols() {
        /*
         * TODO: Complete this method
         * Return the number of columns in the matrix
         */
         int cols;
         cols= mat[0].length;
         return cols;
    }

    int getelem(int i,int j) {
        /*
         * TODO: Complete this method
         * Return the element at row i and column j
         * If i or j is out of bounds, return -1
         */
         if(i>mat.length || j>mat[0].length){
            return -1;
         }
         else{
            return mat[i-1][j-1];
         }
    }

    void setelem(int i,int j, int v) {
        /*
         * TODO: Complete this method
         * Set the element at row i and column j to v
         * If i or j is out of bounds, don't change anything
         */
         if(i<=mat.length || j<=mat[0].length){
            mat[i][j]=v;
         }
    }

    void printmatrix() {
        for(int i=0;i<n;i++) {
            for(int j=0;j<m;j++) {
                if(j!=0) System.out.print(" ");
                System.out.print(mat[i][j]);
            }
            System.out.print("\n") ;
        }
    }
}

