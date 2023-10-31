
public class Array01 {
    private int[] items;
    private int count;
    public Array01(int length){
        items = new int[length];
    }
    public void show(){
         for(int i=0; i<count; i++){
             System.out.println(items[i]);
         }
    }
    public void insertAt(int value){
        //If array is full
        if (items.length==count){
            int[] newItems = new int[count*2];
            for(int i=0; i<count; i++){
                newItems[i] = items[i];
            }
            items = newItems;
        }
        items[count++]=value;
    }
}
