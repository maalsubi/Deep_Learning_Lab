import torch
def cal_minor(mat,row,col):
    lis=[]
    for i in range(len(mat)):
        lis1=[]
        for j in range(len(mat[i])):
            if(i!=row and j!=col):
               lis1.append(mat[i][j])
        lis.append(lis1)
    lis.remove([])
    #print(lis)
    new_data=torch.tensor(lis)
    minor=torch.det(new_data)
    #print(minor)
    return minor

def cal_adj(mat):
    adj=[]
    sign_mat=torch.Tensor([[1,-1,1],[-1,1,-1],[1,-1,1]])
    for i in range(len(mat)):
        lis1=[]
        for j in range(len(mat[i])):
            val=cal_minor(mat,i,j)
            lis1.append(val)
        adj.append(lis1)
    integer_matrix = [[int(element) for element in row] for row in adj]
    integer_tensor = torch.tensor(integer_matrix)
    adjoint_final=(integer_tensor*sign_mat).t()
    print("ADJOINT ID ",adjoint_final)
    return adjoint_final


mat=[[1,-1,2],[2,3,5],[1,0,3]]
mat1=torch.Tensor(mat)
print(mat1)

adjoint=cal_adj(mat1)

inverse_mat=adjoint/torch.det(mat1)
print("INVERSE OF MATRIX ",inverse_mat)