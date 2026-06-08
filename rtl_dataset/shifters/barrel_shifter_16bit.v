module barrel_shifter_16bit(
input [15:0] a,
input [3:0] shift,
output [15:0] y
);

assign y = a << shift;

endmodule