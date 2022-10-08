#include "pch.h"
#include "CppUnitTest.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace UnitTestsubproject
{
	TEST_CLASS(UnitTestsubproject)
	{
	public: //assert strings methods from Node.H
		
		TEST_METHOD(TestMethod1)
		{
			Node("advanced alloy"); //assertion result : Advanced Alloy
		}
	};
}
