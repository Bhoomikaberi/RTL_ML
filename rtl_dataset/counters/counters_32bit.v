module counter_32bit(
input clk,
input rst,
output reg [31:0] count
);

always @(posedge clk or posedge rst)
begin
    if(rst)
        count <= 0;
    else
        count <= count + 1;
end

endmodule