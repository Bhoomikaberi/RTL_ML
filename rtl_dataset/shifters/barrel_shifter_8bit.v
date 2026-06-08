module barrel_shifter_8bit(
input [7:0] a,
input [2:0] shift,
output [7:0] y
);

assign y = a << shift;

endmodule