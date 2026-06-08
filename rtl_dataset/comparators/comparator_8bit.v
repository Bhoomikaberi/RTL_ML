module comparator_8bit(
input [7:0] a,
input [7:0] b,
output gt,
output lt,
output eq
);

assign gt = a > b;
assign lt = a < b;
assign eq = a == b;

endmodule