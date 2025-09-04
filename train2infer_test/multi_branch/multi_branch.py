import paddle
import paddle.nn as nn
import numpy as np


class MultiBranchModel(nn.Layer):
    def __init__(self):
        super().__init__()
        self.backbone = nn.Linear(10, 5)
        self.classifier = nn.Linear(5, 3)  # 分类头
        self.regressor = nn.Linear(5, 1)  # 回归头

    def forward(self, x):
        feat = paddle.tanh(self.backbone(x))  # 共享特征
        cls_out = self.classifier(feat)      # 分支1
        reg_out = self.regressor(feat)       # 分支2
        return cls_out, reg_out              # 两个输出


def main():
    device = paddle.set_device('gpu' if paddle.is_compiled_with_cuda() else 'cpu')

    model = MultiBranchModel()
    model.eval() 

    x_data = np.random.randn(2, 10).astype(np.float32)
    x_tensor = paddle.to_tensor(x_data, place=device)

    input_spec = [paddle.static.InputSpec(shape=[None, 10], dtype=paddle.float32, name='x')]

    static_model = paddle.jit.to_static(
        model,
        input_spec=input_spec,
        full_graph=True
    )

    cls_out, reg_out = static_model(x_tensor)

    # print("Classification output shape:", cls_out.shape)
    # print("Regression output shape:", reg_out.shape)


if __name__ == "__main__":
    main()