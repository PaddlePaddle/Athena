import paddle
import paddle.nn as nn
import numpy as np

class MultiOutputModel(nn.Layer):
    def __init__(self):
        super(MultiOutputModel, self).__init__()

    def forward(self, x):
        a, b = paddle.split(x, num_or_sections=2, axis=1)
        return a, b


def main():
    device = paddle.set_device('gpu') 
   
    model = MultiOutputModel()
    model.eval()  
    
    x_data = np.random.rand(4, 6).astype(np.float32) 
    x_tensor = paddle.to_tensor(x_data, place=device)
    
    input_spec = [paddle.static.InputSpec([4, 6], paddle.float32)]
    
    static_model = paddle.jit.to_static(
        model,
        input_spec=input_spec,
        full_graph=True
    )   
    
    a, b = static_model(x_tensor)

if __name__ == "__main__":
    main()