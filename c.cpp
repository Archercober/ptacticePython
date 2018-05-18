#include <iostream>
 
using namespace std;
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m=nums1.size();int n=nums2.size();
        if(m>n){
            vector<int> temp;

            temp=nums1;
            nums1=nums2;
            nums2=temp;
            int tem=0;
            tem=m;
            m=n;n=tem;
        }
        int i=(m-1)/2;
        int c=(m+n)/2;
        while(true){
            int j=c-i;
            if(i<m&&nums1[i]<nums2[j-1]){
                i=i+1;
            }
            else if(i>0&&nums2[j]<nums1[i-1]) {
                i--;
            }
            else{
                int maxl=0;int minr=0;
                if(i==0){
                    maxl=nums2[j-1];
                    minr=min(nums1[i],nums2[j]);
                }
                else maxl=max(nums1[i-1],nums2[j-1]);
                
                if(i==m){
                    maxl=max(nums1[i-1],nums2[j-1]);
                    
                }else minr=nums2[j];
                
                if ((m+n)%2==0)
                    return (minr+maxl)/2;
                else
                    return minr;
                 
                
                
                
                
            }
        }
    }
    void main{
        cout<<'1';
        printf("ss\n");
    }
};