module left_shifter_8bit(
input [7:0] a,
output [7:0] y
);

assign y = a << 1;

endmodule