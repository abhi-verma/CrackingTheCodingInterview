//O(N)

public class Main {
  public static boolean perm(String str1, String str2) {
    if (str1.length() != str2.length()) {
      return false;
    }
    
    int[] letters = new int[128];
    
    for(int i = 0; i < str1.length(); i++) {
      letters[str1.charAt(i)] += 1;
    }
    
    for(int i = 0; i < str2.length(); i++) {
      if (letters[str2.charAt(i)] < 0) {
        return false;
      }
      letters[str2.charAt(i)] -= 1;
    }
    
    return true;
  }
  
  public static void main(String[] args) {
    String str1 = "abhinav";
    String str2 = "abhivan";
    System.out.println(perm(str1, str2));
  }
}
