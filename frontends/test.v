module xy( clk, in, rst, out_x, out_y );
input clk;
input [3:0] in;
input rst;
output [3:0] out_x;
output [3:0] out_y;

wire   clk;
wire   load;
wire   multi;
wire   load_x;
wire   load_y;

reg   [3:0] x;
reg   [3:0] y;

always @(posedge clk) begin
 //if(load)   x<= in; 
x<= (load)? in: x;
y<= (load)? in: y;
end
wire [3:0] value; 
assign value = (multi?x:y)+1;
always @(posedge clk) begin
if(load_x) out_x<= value;
if(load_y) out_y<= value;
end



reg [1:0] state;
initial state <= 0;
always @(posedge clk) begin
  if(rst) state <= 0;
  else begin
    case(state)
       0: state <= 1;
       1: state <= 2;
       2: state <= 3;
       3: state <= 0;
    endcase
  end
end


assign load = state == 0? 1 : 0;
assign multi = state == 1? 1: 0;
assign load_x = state == 1 ? 1 :0;
assign load_y = state == 2? 1: 0;

assert property ( ! (state == 3) || (  load_x == load_y ));

endmodule

