import java.util.HashMap;
import java.util.Map;

public class morse {

    public static void main(String[] args) {

        Map<String, String> map = new HashMap<String, String>();
        map.put("a", "*- ");
        map.put("b", "-*** ");
        map.put("c", "-*-* ");
        map.put("d", "-** ");
        map.put("e", "* ");
        map.put("f", "**-* ");
        map.put("g", "--* ");
        map.put("h", "**** ");
        map.put("i", "** ");
        map.put("j", "*--- ");

        System.out.println(map.get("a"));
    }

}


