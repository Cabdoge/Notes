# 测试向量转对角矩阵的示例

# 示例 1: 将数值向量转换为对角矩阵
v1 <- c(1, 2, 3, 4)
diag_matrix1 <- diag(v1)
cat("示例 1: 数值向量转对角矩阵\n")
print(diag_matrix1)
cat("\n")

# 示例 2: 使用序列创建对角矩阵
v2 <- 1:5
diag_matrix2 <- diag(v2)
cat("示例 2: 序列转对角矩阵\n")
print(diag_matrix2)
cat("\n")

# 示例 3: 创建单位矩阵
identity_matrix <- diag(5)
cat("示例 3: 创建5×5单位矩阵\n")
print(identity_matrix)
cat("\n")

# 提取对角元素
m <- matrix(1:9, nrow=3, ncol=3)
cat("原始矩阵:\n")
print(m)
diagonal_elements <- diag(m)
cat("对角元素:\n")
print(diagonal_elements)
cat("\n")

# 修改对角元素
m2 <- matrix(1:9, nrow=3, ncol=3)
cat("修改前的矩阵:\n")
print(m2)
diag(m2) <- c(10, 20, 30)
cat("修改对角元素后的矩阵:\n")
print(m2)
