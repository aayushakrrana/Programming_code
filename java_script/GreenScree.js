// write your code here
var bg = new SimpleImage("skyline.jpg");
var fg = new SimpleImage("usain.jpg");

var output = new SimpleImage(fg.getWidth(),fg.getHeight());
for(var pixel of fg.values())
{
    if(pixel.getGreen()>pixel.getRed()+pixel.getBlue())
    {
        var bgpixel = bg.getPixel(pixel.getX(),pixel.getY());
        output.setPixel(pixel.getX(),pixel.getY(),bgpixel);
    }
    else{
        output.setPixel(pixel.getX(),pixel.getY(),pixel);
    }
}
print(output);