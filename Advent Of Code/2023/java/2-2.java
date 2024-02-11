import java.io.*;
import java.util.StringTokenizer;

final class z {
	static int sum = 0;

	public static void main(String[] args) {
		// System.out.println(new File(".").getAbsolutePath());
		try {
			BufferedReader r = new BufferedReader(new FileReader("java/2-2.in"));
			// PrintWriter pw = new PrintWriter("problemname.out");
			for (String line = r.readLine(); line != null; line = r.readLine()) {
				StringTokenizer st = new StringTokenizer(line);
				int red = 0;
				int green = 0;
				int blue = 0;
				int id = 0;
				String current = "";
				while (st.hasMoreTokens()) {
					String token = st.nextToken();
					// System.out.println(token + " test " + token.indexOf(","));
					if (token.indexOf(":") != -1) {
						id = Integer.parseInt(token.substring(0, token.indexOf(":")));
						continue;
					} else if (token.contains("red")) {
						current = token.substring(0, token.length() - 1);
					} else if (token.contains("green")) {
						current = token.substring(0, token.length() - 1);
					} else if (token.contains("blue")) {
						current = token.substring(0, token.length() - 1);
					} else if (!token.contains("Game")) {
						if (current.equals("red")) {
							// System.out.println(token);
							red += Integer.parseInt(token);
						} else if (current.equals("green")) {
							green += Integer.parseInt(token);
						} else if (current.equals("blue")) {
							blue += Integer.parseInt(token);
						}
					}
					// System.out.println(token);
				}
				System.out.println(red + " " + green + " " + blue);
				if (red <= 13 && green <= 13 && blue <= 14) {
					System.out.println("yes");
					sum += id;
				}
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
		System.out.println(sum);
	}
}