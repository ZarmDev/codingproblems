// Source: https://usaco.guide/general/io

import java.io.*;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		OutputStreamWriter fileOutput = new OutputStreamWriter(new FileOutputStream("paint.out"), "UTF-8");
		BufferedReader r = new BufferedReader(new FileReader("paint.in"));
		PrintWriter pw = new PrintWriter(fileOutput);
		StringTokenizer st = new StringTokenizer(r.readLine());
		int a = Integer.parseInt(st.nextToken());
		int b = Integer.parseInt(st.nextToken());
		StringTokenizer st2 = new StringTokenizer(r.readLine());
		int c = Integer.parseInt(st2.nextToken());
		int d = Integer.parseInt(st2.nextToken());

		boolean[] painted = new boolean[100 + 1];
		for (int i = a; i < b; i++) { painted[i] = true; }
		for (int i = c; i < d; i++) { painted[i] = true; }

		int total = 0;
		for (boolean i : painted) { total += i ? 1 : 0; }
		// pw.print("The sum of these three numbers is ");
		pw.println(total);
		/*
		 * Make sure to include the line below, as it
		 * flushes and closes the output stream.
		 */
		pw.close();
	}
}
