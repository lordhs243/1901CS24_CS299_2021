//C++ code to generate dataset of a bank's loan disbursement for beneficiaries
#include<bits/stdc++.h>
#define int long long int

using namespace std;

signed main()
{
    //11 parameters for 10000 beneficiaries

    int dpdt[10000];            //no of dependents
    int grad[10000];            //whether a graduate or not; if not, then 0 and if graduate, then 1
    int self[10000];            //whether self-employed or not; if not, then 0 and if self-employed, then 1
    int incm[10000];            //1/10th of monthly income of beneficiary
    int cinc[10000];            //1/10th of monthly income of co-beneficiary
    int lamt[10000];            //1/10th of loan amount
    int ltrm[10000];            //loan term in months
    int hist[10000];            //credit history; if previous loan disbursed and repaid, then 1 and 0 otherwise
    int pwrt[10000];            //1/10th net property worth
    int p_ar[10000];            //property area; 0 for rural, 1 for semi-urban and 2 for urban
    int stts[10000];            //disbursement status, 1 if loan disbursed to beneficiaries and 0 otherwise

    //all values for a beneficiary are completely random, except the status which is determined by the remaining parameters
    for(int i=0;i<10000;i++)
    {
        dpdt[i]=rand()%6;                   //no of dependents assumed max 5 APART from the beneficiaries
        grad[i]=rand()%2;                   //whether a graduate; grad=0 or 1
        self[i]=rand()%2;                   //whether self-employed; self=0 or 1
        incm[i]=rand()%20000;               //1/10th of monthly income; max assumed 200000
        cinc[i]=rand()%20000;               //1/10th of monthly income; max assumed 200000
        lamt[i]=(rand()%150)*1000;          //1/10th of loan amount; max assumed 1500000
        ltrm[i]=rand()%240;                 //loan terms assumed less than 240
        hist[i]=rand()%2;                   //credit history; hist=0 or 1
        pwrt[i]=(rand()%500)*1000;          //1/10th of property worth; max assumed 5000000
        p_ar[i]=rand()%3;                   //property area; p_ar=0 for rural, 1 for semi-urban and 2 for urban
    }

    //as rand() generates numbers from 0 to 32767, we cannot have 200000 income if we use it directly. So there are 2 options,
    //either to multiply rand() obtained number with 10, which would take max income to 327670, or to store the rand() data as
    //1/10th of the actual amount for all types of amounts, viz., incomes, loan amount and property worth. Here we go for 2nd
    //option in order to keep max monthly income to 200000.

    //income cannot be 0
    for(int i=0;i<10000;i++)
        if(incm[i]==0)
            incm[i]=(incm[i-1]+incm[i+1])/2;

    //income cannot be 0
    for(int i=0;i<10000;i++)
        if(cinc[i]==0)
            cinc[i]=(cinc[i-1]+cinc[i+1])/2;

    //loan amount cannot be 0
    for(int i=0;i<10000;i++)
        if(lamt[i]==0)
            lamt[i]=(lamt[i-1]+lamt[i+1])/2;

    //property worth cannot be 0
    for(int i=0;i<10000;i++)
        if(pwrt[i]==0)
            pwrt[i]=(pwrt[i-1]+pwrt[i+1])/2;

    //loan term must be a multiple of 60(5,10,15 or 20 years terms)
    for(int i=0;i<10000;i++)
    {
        if(ltrm[i]<=60 && ltrm[i]>0)
            ltrm[i]=60;
        else if(ltrm[i]<=120 && ltrm[i]>60)
            ltrm[i]=120;
        else if(ltrm[i]<=180 && ltrm[i]>120)
            ltrm[i]=180;
        else if(ltrm[i]<=240 || ltrm[i]==0)
            ltrm[i]=240;
    }

    //determining disbursement status based on remaining parameters
    for(int i=0;i<10000;i++)
    {
        //scores for different parameters as explained, repayment capability is most prior so its weight is 3 if achieved, area
        //of property comes thereafter, and score equals the type of area, then priorities are minimal no of dependents and
        //credit history, so they are weighted at 2 if achieved and least priority is being a graduate and self-employed so
        //their score is 1 if achieved; if any parameter is not achieved its score is default set to 0

        int pay=0;          //whether beneficiary can smoothly repay based on incomes, loan term,loan amount and property worth
        int dep=0;          //no of dependents goes up, repayment gets more rough
        int gra=0;          //if well educated then smooth job so smooth repayment
        int sel=0;          //if self-employed then job security so smooth repayment
        int his=0;          //if previous loan was repaid, then a responsible beneficiary so smooth repayment
        int p_a=0;          //property areas urban is more preferred than semi-urban which is more preferred than rural

        //assuming 33% EMI for beneficiary, 25% EMI for co-beneficiary and monthly property mortgage, if exceeds the monthly loan
        //amount and simple interest at a standard rate of 10% then repayment is capable and set score of repayment capability to
        //3 hence. Note that since all values are 1/10th of their actual, the expression would be unaffected if we use the values
        //assuming they only are actual, and that is also the very reason why we stored 1/10th of all amount values.
        if(incm[i]/3+cinc[i]/4+(pwrt[i]/ltrm[i])>=(lamt[i]/ltrm[i])+(lamt[i]/120))
            pay=3;

        //if no of dependents is less than 3, we classify as minimal dependency and set score of minimal dependency to 2
        if(dpdt[i]<3)
            dep=2;

        //if graduate, set score of education as 1
        if(grad[i]==1)
            gra=1;

        //if self-employed, set score of job security as 1
        if(self[i]==1)
            sel=1;

        //if credit history is clean, set score of responsiblity to 2
        if(hist[i]==1)
            his=2;

        //property area score is same as the type of area; 2 for urban, 1 for semi-urban and 0 for rural
        p_a+=p_ar[i];

        //net score is sum of scores
        int net=(pay+dep+gra+sel+his+p_a);

        //if net score is more than the natural-optimal threshold as ceil(max total score/2), loan is assumed to be disbursed and
        //status is thus set to 1
        if(net>6)
            stts[i]=1;
        else
            stts[i]=0;
    }

    //the data in the arrays can be set to output by the program by simple iteration and the data is stored in text files
    //separately for each type of data

    return 0;
}
