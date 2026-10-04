#include <iostream>
#include <stack>
#include <string>
#include <unordered_map>
#include <cassert>
using namespace std;

bool isBalanced(const string& s) {
    unordered_map<char, char> match = {{')', '('}, {']', '['}, {'}', '{'}};
    stack<char> st;

    for (char c : s) {
        if (c == '(' || c == '[' || c == '{') {
            st.push(c);
        } else if (match.count(c)) {
            if (st.empty() || st.top() != match[c]) {
                return false;
            }
            st.pop();
        }
       
    }
    return st.empty();
}

int main() {
    cout << isBalanced("([{}])") << endl;
    cout << isBalanced("([)]") << endl;

    return 0;
}
