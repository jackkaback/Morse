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
		map.put("k", "-*- ");
		map.put("l", "*-** ");
		map.put("m", "-- ");
		map.put("n", "-* ");
		map.put("o", "--- ");
		map.put("p", "*--* ");
		map.put("q", "--*- ");
		map.put("r", "*-* ");
		map.put("s", "*** ");
		map.put("t", "- ");
		map.put("u", "**- ");
		map.put("v", "***- ");
		map.put("w", "*-- ");
		map.put("x", "-**- ");
		map.put("y", "-*-- ");
		map.put("z", "--** ");
		map.put("0", "----- ");
		map.put("1", "*---- ");
		map.put("2", "**--- ");
		map.put("3", "***-- ");
		map.put("4", "****- ");
		map.put("5", "***** ");
		map.put("6", "-**** ");
		map.put("7", "--*** ");
		map.put("8", "---** ");
		map.put("9", "----* ");
		map.put(".", "*-*-*- ");
		map.put("?", "**--** ");
		map.put(" ", "\t");

		System.out.println(map.get("a"));
	}

}
